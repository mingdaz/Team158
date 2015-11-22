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
from django.template import loader, Context
# from grumblr.models import *
from datetime import datetime	
# from forms import *
from mimetypes import guess_type
from django.core.mail import send_mail
from django.conf import settings
from django.core import serializers
from account.models import *
from forms import * 
from models import * 

@login_required
def homepage(request):
	context = {}
	return redirect('dashboard')

@login_required
def get_test(request,level):
	context = {}
	context['username'] = request.user.username
	cur_user = User.objects.get(username__exact = context['username'])
	learner = Learner.objects.get(user = cur_user)
	context['cur_user'] = learner
	# newtest = Test.objects.filter(level = level)
	# context['test_id'] = newtest[5].id;
	# context['qnum'] = len(newtest[5].question.all());
	
	return render(request, 'testpage/test.html', context)

@login_required
def get_learn(request,level,lesson):
	context = {}
	context['username'] = request.user.username
	cur_user = User.objects.get(username__exact = context['username'])
	learner = Learner.objects.get(user = cur_user)
	context['cur_user'] = learner
	return render(request, 'testpage/learn.html', context)

@login_required
def get_result(request):
	context = {}
	return render(request, 'testpage/learn.html', context)

@login_required
def test_create(request):
	context = {}
	context['username'] = request.user.username
	context['flag'] = 1
	context['chooselevel'] = TestLevelForm()
	return render(request, 'testpage/post_question.html', context)

@login_required
def test_add_question_mc(request):
	itemTemplate = loader.get_template('multichoice.html')
	new_question = Question(qtype="mc");
	new_question.save()
	maxid = new_question.id
	print maxid
	item = itemTemplate.render({"id":maxid,"form":MCQFrom()}).replace('\n','').replace('\"','\'') #More escaping might be needed
	return render(request, 'item.json', {"item":item,"id":maxid,"flag":1}, content_type='application/json')
	
@login_required
def test_add_question_tr(request):
	itemTemplate = loader.get_template('translate.html')
	new_question = Question(qtype="tr");
	new_question.save()
	maxid = new_question.id
	item = itemTemplate.render({"id":maxid,"form":TRQFrom()}).replace('\n','').replace('\"','\'') #More escaping might be needed
	return render(request, 'item.json', {"item":item,"id":maxid,"flag":1}, content_type='application/json')

@login_required
def test_save_mc_question(request,id):
	mcqform = MCQFrom(request.POST);
	flag = 0
	if mcqform.is_valid():
		new_question = Question.objects.get(id=id)
		new_question.question=mcqform.cleaned_data['question']
		new_question.a=mcqform.cleaned_data['a']
		new_question.b=mcqform.cleaned_data['b']
		new_question.c=mcqform.cleaned_data['c']
		new_question.d=mcqform.cleaned_data['d']
		new_question.answer=request.POST['optionsRadiosInline']
		new_question.explanation=mcqform.cleaned_data['explanation']
		new_question.save()
		flag = 1
	itemTemplate = loader.get_template('multichoice.html')
	item = itemTemplate.render({"id":id,"form":mcqform}).replace('\n','').replace('\"','\'') #More escaping might be needed
	return render(request, 'item.json', {"item":item,"id":id,"flag":flag}, content_type='application/json')

@login_required
def test_save_tr_question(request,id):
	trqform = TRQFrom(request.POST);
	flag = 0
	if trqform.is_valid():
		new_question = Question.objects.get(id=id)
		new_question.question=trqform.cleaned_data['question']
		new_question.explanation=trqform.cleaned_data['explanation']
		new_question.save()
		flag = 1
	itemTemplate = loader.get_template('translate.html')
	item = itemTemplate.render({"id":id,"form":trqform}).replace('\n','').replace('\"','\'') #More escaping might be needed
	return render(request, 'item.json', {"item":item,"id":id,"flag":flag}, content_type='application/json')

@login_required
def test_edit_question(request):
	context = {}
	context['username'] = request.user.username
	return render(request, 'testpage/post_question.html', context)

@login_required
def test_delete_question(request,id):
	try:
		x = Question.objects.get(id=id)
		x.delete()
	except Question.DoesNotExist:
		x = None
	return render(request, 'item.json', {"item":"","id":id,"flag":1}, content_type='application/json')

@login_required
def get_test_post_id(request):
	newtest = Test.objects.create()
	newtest.save()
	id = newtest.id
	print id
	return render(request, 'item.json', {"item":"","id":id,"flag":1}, content_type='application/json')

@login_required
def test_post(request,test_id,question_id):
	try:
		x = Test.objects.get(id=test_id)
		y = Question.objects.get(id=question_id)
		x.question.add(y)
		flag = 1
	except Question.DoesNotExist:
		flag=0
	return render(request, 'item.json', {"item":"","id":0,"flag":flag}, content_type='application/json')

@login_required
def test_set_level(request,test_id):
	x = Test.objects.get(id=test_id)
	form = TestLevelForm(request.POST)
	if form.is_valid():
		x.level = form.cleaned_data['test_level']
		x.save()
		flag = 1
		print "valid"
	else:
		flag = 0
	return render(request, 'item.json', {"item":"","id":0,"flag":flag}, content_type='application/json')

@login_required
def next_questions(request):
	# print request.POST
	qid = int(request.POST['qid'])
	qnum = int(request.POST['qnum'])
	if qid==-1:
		qnum = 0
		learner = Learner.objects.get(user__exact = request.user)
		newtest = Test.objects.filter(level = learner.current_level)[6]
		qid = newtest.id
		question = newtest.question.all()[0]
		length = len(newtest.question.all())
	else:
		print "else"
		newtest = Test.objects.get(id = qid)
		length = len(newtest.question.all())
		if qnum<length:
			question = newtest.question.all()[qnum]
		else:
			question = newtest.question.all()[0]
	qtype = question.qtype
	qnum = qnum+1
	if qtype=="tr":
		itemTemplate = loader.get_template('test-tr.html')
	else:
		itemTemplate = loader.get_template('test-mc.html')

	item = itemTemplate.render({"item":question}).replace('\n','').replace('\"','\'') #More escaping might be needed
	return render(request, 'testcontent.json', {"item":item,"id":qid,"flag":1,"qnum":qnum,"max":length}, content_type='application/json')

@login_required
def get_learning(request):
	context = {}
	context['username'] = request.user.username
	return render(request, 'testpage/learn.html', context)

@login_required
def get_learning(request):
	context = {}
	context['username'] = request.user.username
	return render(request, 'testpage/learn.html', context)

@login_required
def get_learningResult(request):
	context = {}
	context['username'] = request.user.username
	return render(request, 'testpage/learn.html', context)

@login_required
def skip_question(request):
	context = {}
	context['username'] = request.user.username
	return render(request, 'testpage/learn.html', context)

@login_required
def exit_learning(request):
	context = {}
	context['username'] = request.user.username
	return render(request, 'testpage/learn.html', context)

@login_required
def show_tips(request):
	context = {}
	context['username'] = request.user.username
	return render(request, 'testpage/learn.html', context)

@login_required
def get_discussion(request):
	context = {}
	context['username'] = request.user.username
	return render(request, 'testpage/learn.html', context)

@login_required
def create_learning(request):
	context = {}
	context['username'] = request.user.username
	return render(request, 'testpage/learn.html', context)

@login_required
def learning_add_question(request):
	context = {}
	context['username'] = request.user.username
	return render(request, 'testpage/learn.html', context)

@login_required
def learning_save_question(request):
	context = {}
	context['username'] = request.user.username
	return render(request, 'testpage/learn.html', context)

@login_required
def learning_edit_question(request):
	context = {}
	context['username'] = request.user.username
	return render(request, 'testpage/learn.html', context)

@login_required
def learning_delete_question(request):
	context = {}
	context['username'] = request.user.username
	return render(request, 'testpage/learn.html', context)

@login_required
def learning_post(request):
	context = {}
	context['username'] = request.user.username
	return render(request, 'testpage/learn.html', context)

