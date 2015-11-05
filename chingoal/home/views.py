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
@login_required
def home(request):
    context = {}
    cur_user = request.user
    context['scheduleForm'] = EditScheduleForm()
    if Learner.objects.filter(user = request.user):
        learner = Learner.objects.filter(user = cur_user)
        context['cur_user'] = learner
    if Teacher.objects.filter(user = request.user):
        teacher = Teacher.objects.filter(user = cur_user)
        context['cur_user'] = teacher
    return render(request, 'home.html', context)