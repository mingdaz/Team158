from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse

import json

from models import *
from forms import *

def register(request):
    context = {}
    if request.method == 'GET':
        context['register_form'] = RegistrationForm()
        return render(request, 'account/register.html', context)
    
    register_form = RegistrationForm(request.POST, request.FILES)
    context['register_form'] = register_form

    if not register_form.is_valid():
        return render(request, 'account/register.html', context)

    new_user = User.objects.create_user(username=register_form.cleaned_data['username'],
                                    password=register_form.cleaned_data['password1'],
                                    email=register_form.cleaned_data['email'])
    new_user.save()
    if request.POST['optionsRadiosInline'] == 'option1':
        identity = 0
    elif request.POST['optionsRadiosInline'] == 'option2':
        identity = 1

    if identity == 0:
        new_learner = Learner.objects.create(user=new_user)
        new_learner.save()
    elif identity == 1:
        new_teacher = Teacher.objects.create(user=new_user)
        new_teacher.save()
    
    new_user = authenticate(username=register_form.cleaned_data['username'], \
                                password=register_form.cleaned_data['password1'])
    login(request, new_user)
    return redirect('/')

@login_required
def edit_profile(request):
    if request.method == 'GET':
        return render(request, 'account/edit_profile.html', {'editForm': EditProfileForm()})

    edit_form = EditProfileForm(request.POST, request.FILES)
    errors = []

    if not request.user.check_password(request.POST['password1']):
        errors.append('Old password is incorrect.')
    
    if errors:
        return render(request, 'account/edit_profile.html', {'errors':errors, 'editForm': edit_form})

    if not edit_form.is_valid():
        return render(request, 'account/edit_profile.html',{'editForm': edit_form})
    
    if edit_form.cleaned_data['password2']:
        request.user.set_password(edit_form.cleaned_data['password2'])

    if edit_form.cleaned_data['photo']:
        new_photo = edit_form.cleaned_data['photo']
        if Learner.objects.filter(user = request.user):
            request.user.learner_user.photo = new_photo
        elif Teacher.objects.filter(user = request.user):
            request.user.teacher.photo = new_photo

    if edit_form.cleaned_data['bio']:
        new_bio = edit_form.cleaned_data['bio']
        if Learner.objects.filter(user = request.user):
            request.user.learner_user.bio = new_bio
        elif Teacher.objects.filter(user = request.user):
            request.user.teacher.bio = new_bio

    request.user.save()
    if Learner.objects.filter(user = request.user):
        request.user.learner_user.save()
    elif Teacher.objects.filter(user = request.user):
        request.user.teacher.save()

    errors.append('Changes are saved successfully. Please login again.')
    return render(request, 'account/edit_profile.html', {'errors':errors, 'editForm': EditProfileForm()})

@login_required
def view_profile(request, uname):
    context = {}
    cur_user = User.objects.get(username__exact = uname)
    context['username'] = uname
    context['cur_username'] = request.user.username
    if Learner.objects.filter(user = cur_user):
        learner = Learner.objects.get(user = cur_user)
        context['cur_user'] = learner
        if learner.follows.filter(username__exact = uname):
            context['isFollowing'] = 'yes'
        else:
            context['isFollowing'] = 'no'
        context['history'] = History.objects.filter(user = cur_user)
        context['isLearner'] = 'yes'

    elif Teacher.objects.filter(user=cur_user):
        teacher = Teacher.objects.get(user = cur_user)
        context['cur_user'] = teacher
        if teacher.follows.filter(username__exact = uname):
            context['isFollowing'] = 'yes'
        else:
            context['isFollowing'] = 'no'
        context['history'] = History.objects.filter(user = cur_user)
        context['isLearner'] = 'no'

    return render(request, 'account/view_profile.html', context)

def reset_password(request):
    context = {}
    return render(request, 'resetPassword.html', context)

def new_password(request,token):
    return redirect('/')

@login_required
def edit_schedule(request):
    if request.method == 'GET':
        return HttpResponse("Please add something by POST method.")

    scheduleForm = EditScheduleForm(request.POST)

    if scheduleForm.is_valid():
        pass

    if scheduleForm.cleaned_data['progress_level']:
        progress_level = scheduleForm.cleaned_data['progress_level']
        request.user.learner_user.progress_level = progress_level

    if scheduleForm.cleaned_data['progress_lesson']:
        progress_lesson = scheduleForm.cleaned_data['progress_lesson']
        request.user.learner_user.progress_lesson = progress_lesson
    request.user.learner_user.save()
    return redirect('/')

@login_required
def follow(request, uname, isFollowing, isLearner):
    followee = User.objects.get(username__exact = uname)
    if isLearner == 'yes':
        follower = request.user.learner
    else:
        follower = request.user.teacher

    if isFollowing == 'yes':
        if follower.follows.filter(username__exact = followee.username):
            follower.follows.remove(followee)
            follower.save()
    else:
        if not follower.follows.filter(username__exact = followee.username):
            follower.follows.add(followee)
            follower.save()
    return redirect(reverse('viewProfile', kwargs = {'uname':uname}))

