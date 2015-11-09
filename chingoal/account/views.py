from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.views import password_reset, password_reset_confirm,password_change_done
import json
import hashlib, random

from models import *
from forms import *
from django.shortcuts import render_to_response, get_object_or_404

def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request, template_name='account/reset_confirm.html',
        uidb64=uidb64, token=token, post_reset_redirect=reverse('home'))

def reset(request):
    return password_reset(request, template_name='account/reset.html',
        email_template_name='account/reset_email.html',
        subject_template_name='account/reset_subject.txt',
        post_reset_redirect=reverse('home'))

# def reset(request):
#     return password_change_done(request, template_name='account/password_change_done.html')


def register(request):
    context = {}
    if request.method == 'GET':
        context['register_form'] = RegistrationForm()
        return render(request, 'account/register.html', context)
    
    register_form = RegistrationForm(request.POST)
    context['register_form'] = register_form

    if not register_form.is_valid():
        return render(request, 'account/register.html', context)
    register_form.save()
    username=register_form.cleaned_data['username']
    email=register_form.cleaned_data['email']
    salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
    activation_key = hashlib.sha1(salt+email).hexdigest()
    new_user=User.objects.get(username=username)
    if request.POST['optionsRadiosInline'] == 'option1':
        identity = 0
    elif request.POST['optionsRadiosInline'] == 'option2':
        identity = 1

    if identity == 0:
        new_learner = Learner.objects.create(user=new_user)
        new_learner.save()
        new_user = authenticate(username=register_form.cleaned_data['username'], \
                                    password=register_form.cleaned_data['password1'])
        login(request, new_user)
        return redirect('/home')

    elif identity == 1:
        new_teacher = Teacher.objects.create(user=new_user,activation_key=activation_key)
        new_teacher.save()
        email_subject = 'Account confirmation'
        email_body = "Hey %s, thanks for signing up. To activate your account, click this link within \
            48hours http://127.0.0.1:8000/account/confirm/%s" % (register_form.cleaned_data['username'], activation_key)
            
        send_mail(email_subject, email_body, '15637test@gmail.com',
                      [register_form.cleaned_data['email']], fail_silently=False)
                      
        return redirect(reverse('login'))


@login_required
def edit_profile(request):
    if Learner.objects.filter(user = request.user):
        flag = 0
    else:
        flag = 1
    if request.method == 'GET':
        return render(request, 'account/edit_profile.html', {'editForm': EditProfileForm(),'username':request.user.username,'flag':flag})

    edit_form = EditProfileForm(request.POST, request.FILES)
    errors = []
    if not request.user.check_password(request.POST['password1']):
        errors.append('Old password is incorrect.')
    
    if errors:
        return render(request, 'account/edit_profile.html', {'errors':errors, 'msg':'no','editForm': edit_form,'username':request.user.username,'flag':flag})

    if not edit_form.is_valid():
        return render(request, 'account/edit_profile.html',{'editForm': edit_form, 'msg':'no','username':request.user.username,'flag':flag})
    
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
    return render(request, 'account/edit_profile.html', {'errors':errors, 'msg':'yes','editForm': EditProfileForm(),'username':request.user.username,'flag':flag})

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
            followers = Learner.objects.filter(user__in=request.user.learner_user.follows.all()).reverse()
            context['followers'] = followers
        else:
            context['isFollowing'] = 'no'
        context['history'] = History.objects.filter(user = cur_user)
        context['isLearner'] = 'yes'
        context['scheduleForm'] = EditScheduleForm(initial={'progress_level':learner.progress_level,'progress_lesson':learner.progress_lesson})


    elif Teacher.objects.filter(user=cur_user):
        teacher = Teacher.objects.get(user = cur_user)
        context['cur_user'] = teacher
        if teacher.follows.filter(username__exact = uname):
            context['isFollowing'] = 'yes'
            followers = Teacher.objects.filter(user__in=request.user.teacher.follows.all()).reverse()
            context['followers'] = followers
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
    return redirect(reverse('viewProfile', kwargs = {'uname':request.user.username}))

@login_required
def follow(request, uname, isFollowing, isLearner):
    followee = User.objects.get(username__exact = uname)
    if isLearner == 'yes':
        follower = request.user.learner_user
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

@login_required
def post_question(request):
    errors = None
    if not 'text' in request.POST or not request.POST['text']:
        errors = 'You must enter something.'
    else:
        if len(request.POST['text']) > 42:
            errors = 'You post message need to 42 characters or less.'
            context = {'posts': Grumblr.objects.all().order_by('-time')}
            context['add_post_errors'] = errors
            return render(request, 'grumblr/global_stream.html', context)
        else:
            new_post = Grumblr(user=request.user, content=request.POST['text'])
            new_post.save()
    newUser = UserProfile.objects.get(user=request.user)
    context = {'posts': Grumblr.objects.all().order_by('-time')}
    context['add_post_errors'] = errors
    context['newUser'] = newUser
    return render(request, 'grumblr/global_stream.html', context)

def register_confirm(request, activation_key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.user.is_authenticated():
        HttpResponseRedirect('/home')
    
    # check if there is UserProfile which matches the activation key (if not then display 404)
    teacher = get_object_or_404(Teacher, activation_key=activation_key)

    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = teacher.user
    user.is_active = True
    user.save()
    return render_to_response('account/confirm.html')