from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from account.models import *
# Create your views here.
@login_required
def home(request):
    context = {}
    cur_user = request.user.learner_user
    context['cur_user'] = cur_user
    return render(request,'store/store.html',context)

@login_required
def buy_title(request, title, cost):
    learner = request.user.learner_user
    money = learner.user_vm
    learner.title = title
    learner.user_vm = money - int(cost)
    learner.save()
    return redirect('/store')

@login_required
def unlock_learning(request, lesson):
    learner = request.user.learner_user
    money = learner.user_vm
    learner.unlock = lesson
    learner.user_vm = money - 5
    learner.save()
    return redirect('/store')
