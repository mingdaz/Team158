from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse

import json

from basic.post_models import *
from basic.question_models import *
from basic.user_models import *
from basic.message_models import *

@login_required
def home(request):
    context = {}
    return render(request, 'home.html', context)

def register(request):
    context = {}
    if request.method == 'GET':
        context['register_form'] = RegistrationForm()
        return render(request, 'register.html', context)
    
    register_form = RegistrationForm(request.POST, request.FILES)
    context['register_form'] = register_form

    if not register_form.is_valid():
        return render(request, 'register.html', context)

    new_user = User.objects.create_user(username=register_form.cleaned_data['username'],
                                    password=register_form.cleaned_data['password1'],
                                    email=register_form.cleaned_data['email'])
    new_user.save()
    identity = register_form.cleaned_data['identity']

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
    context = {}
    return render(request, 'home.html', context)

@login_required
def view_profile(request, uname):
    context = {}
    return render(request, 'home.html', context)

def reset_password(request):
    context = {}
    return render(request, 'resetPassword.html', context)

def new_password(request,token):
    return redirect('/')

@login_required
def edit_schedule(request):
    context = {}
    return render(request, 'home.html', context)

@login_required
def add_follower(request, uname):

    return redirect(reverse('viewProfile', kwargs = {'uname':uname}))

@login_required
def remove_follower(request, uname):

    return redirect(reverse('viewProfile', kwargs = {'uname':uname}))