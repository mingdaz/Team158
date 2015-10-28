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