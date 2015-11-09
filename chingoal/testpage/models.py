from django.db import models
from django.db.models import Max
# Create your models here.
# class Word_Translation(models.Model):
# 	question = models.CharField(max_length=200)
# 	answer = models.CharField(max_length=200)
# 	explanation = models.CharField(max_length=200)
# 	def __unicode__(self):
# 		return self.text

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
	def __unicode__(self):
		return self.text

class Test(models.Model):
	level = models.IntegerField(default=0)
	question = models.ManyToManyField(Question)
	def __unicode__(self):
		return self.text

	@staticmethod
	def get_max_id():
		print "get max id"
		return Test.objects.all().aggregate(Max('id'))['id__max'] or 0


class Learn(models.Model):
	lock = models.IntegerField()
	question = models.ManyToManyField(Question)
	def __unicode__(self):
		return self.text
