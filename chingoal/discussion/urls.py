
from django.conf.urls import include, url

urlpatterns = [
    url(r'^post-question$','discussion.views.post_question',name ='post' ),
    url(r'^reply-question$','discussion.views.reply_question',name ='learningsavequestion' ),
    url(r'^delete-post$','discussion.views.delete_post',name ='learningeditquestion' ),
    url(r'^$', 'discussion.views.discussion_home', name = 'discussion_home'),
   ]
