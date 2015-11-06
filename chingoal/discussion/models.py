from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=500)
    text = models.CharField(max_length=500)
    post_time = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User)
    # tag = models.CharField(max_length = 200)
    
    def __unicode__(self):
        return self.author + ',' + self.postTime

    @staticmethod
    def get_max_id():
        return Post.objects.all().aggregate(Max('id'))['id__max'] or 0

    @staticmethod
    def get_changed_posts(max_id):
        return Post.objects.filter(id__gt=max_id).distinct()

    # @property
    # def html(self):
    #     postTemplate = loader.get_template('grumblr/post_base.html')
    #     context = Context({'post': self})
    #     return postTemplate.render(context).replace('\n','').replace('"', '&quot;')


class Reply(models.Model):
    text = models.CharField(max_length=500)
    post_time = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User)
    reply_to = models.ForeignKey(Post)
    
    def __unicode__(self):
        return self.author + ',' + self.postTime

    @staticmethod
    def get_replies(postid):
        return Reply.objects.filter(post_id = postid)

    # @property
    # def html(self):
    #     replyTemplate = loader.get_template('grumblr/reply_base.html')
    #     context = Context({'reply':self})
    #     return replyTemplate.render(context).replace('\n','').replace('"', '&quot;')