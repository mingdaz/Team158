from django.db import models

from django.contrib.auth.models import User

from basic.user_models import *

class message(models.Model):
    author = models.ForeignKey(User)
    text = models.CharField(max_length = 4200)
    post_time = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.author + '@' + self.post_time
        