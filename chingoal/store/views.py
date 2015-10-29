from django.shortcuts import render
from django.http import HttpResponse

from models import *
# Create your views here.
@login_required
def buy_title(request):
    context = {}
    return render(request,'store.html',context)

@login_required
def unlock_learning(request):
    context = {}
    return render(request,'store.html',context)

@login_required
def earn_money(request):
    return HttpResponse('success')