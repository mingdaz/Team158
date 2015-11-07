from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.contrib.auth.views import password_reset, password_reset_confirm
# Decorator to use built-in authentication system
from django.contrib.auth.decorators import login_required
# from django.db.models import Q
# Used to create and manually log in a user
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.db.models import Count
from django.db import transaction
# from grumblr.models import *
from datetime import datetime	
# from forms import *
from mimetypes import guess_type
from django.core.mail import send_mail
from django.conf import settings
from django.core import serializers

@login_required
def homepage(request):
	context = {}
	return redirect('dashboard')

@login_required
def get_test(request):
	context = {}
	context['username'] = request.user.username
	return render(request, 'testpage/learn.html', context)

@login_required
def get_learn(request,level,lesson):
	context = {}
	context['username'] = request.user.username
	return render(request, 'testpage/learn.html', context)

@login_required
def get_result(request):
	context = {}
	return render(request, 'testpage/learn.html', context)

@login_required
def test_create(request):
	context = {}
	return render(request, 'testpage/post_question', context)

@login_required
def test_add_question(request):
	context = {}
	return render(request, 'testpage/post_question', context)

@login_required
def test_save_question(request):
	context = {}
	return render(request, 'testpage/post_question', context)

@login_required
def test_edit_question(request):
	context = {}
	return render(request, 'testpage/post_question', context)

@login_required
def test_delete_question(request):
	context = {}
	return render(request, 'testpage/post_question', context)

@login_required
def test_post(request):
	context = {}
	return render(request, 'testpage/post_question', context)

@login_required
def get_learning(request):
	context = {}
	return render(request, 'testpage/learn.html', context)

@login_required
def get_learning(request):
	context = {}
	return render(request, 'testpage/learn.html', context)

@login_required
def get_learningResult(request):
	context = {}
	return render(request, 'testpage/learn.html', context)

@login_required
def skip_question(request):
	context = {}
	return render(request, 'testpage/learn.html', context)

@login_required
def exit_learning(request):
	context = {}
	return render(request, 'testpage/learn.html', context)

@login_required
def show_tips(request):
	context = {}
	return render(request, 'testpage/learn.html', context)

@login_required
def get_discussion(request):
	context = {}
	return render(request, 'testpage/learn.html', context)

@login_required
def create_learning(request):
	context = {}
	return render(request, 'testpage/learn.html', context)

@login_required
def learning_add_question(request):
	context = {}
	return render(request, 'testpage/learn.html', context)

@login_required
def learning_save_question(request):
	context = {}
	return render(request, 'testpage/learn.html', context)

@login_required
def learning_edit_question(request):
	context = {}
	return render(request, 'testpage/learn.html', context)

@login_required
def learning_delete_question(request):
	context = {}
	return render(request, 'testpage/learn.html', context)

@login_required
def learning_post(request):
	context = {}
	return render(request, 'testpage/learn.html', context)

