from django.db import models
from django.db.models import Max
from account import teacher

class Question(models.Model):
	level = models.IntegerField(default=0)
	qtype = models.CharField(max_length=200)
	question = models.CharField(max_length=200)
	a = models.CharField(max_length=200)
	b = models.CharField(max_length=200)
	c = models.CharField(max_length=200)
	d = models.CharField(max_length=200)
	answer = models.CharField(max_length=200)
	explanation = models.CharField(max_length=200)
	saveflag = models.CharField(max_length=10)
	def __unicode__(self):
		return self.text

class Test(models.Model):
	level = models.IntegerField(default=0)
	question = models.ManyToManyField(Question)
	postflag = models.CharField(max_length=10)
	teacher = models.ManyToManyField(teacher)
	def __unicode__(self):
		return self.text

	@staticmethod
	def get_max_id():
		print "get max id"
		return Test.objects.all().aggregate(Max('id'))['id__max'] or 0


class Learn(models.Model):
	lock = models.IntegerField(default = 1)
	level = models.IntegerField(default = 0)
	lesson = models.IntegerField(default = 1)
	lnum = models.IntegerField(default = 0)
	ltype = models.CharField(max_length=10)
	# Two types: text or audio
	text = models.CharField(max_length=200)
	a = models.CharField(max_length=200, blank = True)
	b = models.CharField(max_length=200, blank = True)
	c = models.CharField(max_length=200, blank = True)
	image1 = models.ImageField(blank = True)
	image2 = models.ImageField(blank = True)
	image3 = models.ImageField(blank = True)
	audio = models.FileField(blank = True)

	def __unicode__(self):
		return self.level + ' ' + self.lesson + ' ' + self.lid

class QuestionAnswer(models.Model):
	username = models.CharField(max_length=200)
	qid = models.CharField(max_length=200)
	answer = models.CharField(max_length=200)
	correctness = models.CharField(max_length=10)

class TestAnswer(models.Model):
	username = models.CharField(max_length=200)
	tid = models.CharField(max_length=200)
	question = models.ManyToManyField(QuestionAnswer)
