from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from models import *
# Create your views here.
@login_required
def home(request):
    context = {}
    return render(request,'store/store.html',context)

@login_required
def buy_title(request):
    context = {}
    return render(request,'store/store.html',context)

@login_required
def unlock_learning(request):
    context = {}
    return render(request,'store/store.html',context)

@login_required
def earn_money(request):
    return HttpResponse('success')