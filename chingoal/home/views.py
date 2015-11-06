from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse

import json

from account.models import *
from account.forms import *

# Create your views here.
def homepage(request):
    context = {}
    return render(request, 'home.html', context)

@login_required
def home(request):
    context = {}
    cur_user = request.user
    
    context['username'] = cur_user.username
    if Learner.objects.filter(user = request.user):
        learner = Learner.objects.get(user = cur_user)
        context['cur_user'] = learner
        context['scheduleForm'] = EditScheduleForm(initial={'progress_level':learner.progress_level,'progress_lesson':learner.progress_lesson})
    
    if Teacher.objects.filter(user = request.user):
        teacher = Teacher.objects.get(user = cur_user)
        context['cur_user'] = teacher


    return render(request, 'dashboard.html', context)