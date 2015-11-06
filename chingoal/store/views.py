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
def buy_title(request, title):
    request.user.learner_user.title = title
    request.user.learner_user.save()
    return render(request,'store/store.html',context)

@login_required
def unlock_learning(request, lesson):
    print lesson
    request.user.learner_user.unlock = lesson
    request.user.learner_user.save()
    return redirect('/store')

@login_required
def earn_money(request):
    return HttpResponse('success')