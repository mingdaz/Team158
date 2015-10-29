from django.db import models

from django.contrib.auth.models import User

class Learner(models.Model):
    user = models.OneToOneField(User, unique = True, related_name = 'learner_user')  
    TITLE_CHOICES = (('A', 'Primary School'), ('B', 'Middle School'), \
        ('C', 'High School'), ('D', 'College'))  
    title = models.CharField(max_length = 20, default = TITLE_CHOICES[0][0], choices = TITLE_CHOICES)
    progress_level = models.IntegerField(default = 1)
    progress_lesson = models.IntegerField(default = 1)
    user_vm = models.IntegerField(default = 0)
    lesson_plan = models.IntegerField(default = 1)  # MAX = 5
    follows = models.ManyToManyField(User,related_name = 'learner_follows')
    photo = models.ImageField(upload_to = 'user_photo', blank = True)

    def __unicode__(self):
        return 'Learner' + self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(User, unique = True)
    bio = models.CharField(max_length = 420, default='Please introduce yourself')
    photo = models.ImageField(upload_to = 'user_photo', blank = True)

    def __unicode__(self):
        return 'Teacher' + self.user.username

