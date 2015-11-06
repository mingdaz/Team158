from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from models import *
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
    return redirect('/')

@login_required
def unlock_learning(request, lesson):
    if lesson == "One lesson":
        unlock = 1
    elif lesson == "Two lessons":
        unlock = 2
    elif lesson == "Three lessons":
        unlock = 3
    elif lesson == "Four lessons":
        unlock = 4
    elif lesson == "Five lessons":
        unlock = 5
    request.user.learner_user.unlock = unlock
    request.user.learner_user.save()
    return redirect('/')

@login_required
def earn_money(request):
    return HttpResponse('success')