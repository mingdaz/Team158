
from django.conf.urls import include, url

urlpatterns = [
    url(r'^post-question$','discussion.views.post_question',name ='post' ),
    url(r'^reply-question$','discussion.views.reply_question',name ='learningsavequestion' ),
    url(r'^delete-post$','discussion.views.delete_post',name ='learningeditquestion' ),
    url(r'^$', 'discussion.views.discussion_home', name = 'discussion_home'),
    url(r'^discussion_reply/(?P<post_id>\d+)$', 'discussion.views.discussion_reply', name = 'discussion_reply'),
    url(r'^get_posts$', 'discussion.views.get_posts', name = 'get_posts'),
    url(r'^post_post$', 'discussion.views.post_post', name = 'post_post'),
    url(r'^discussion_reply/post_reply$', 'discussion.views.post_reply', name = 'post_reply'),
    url(r'^discussion_reply/get_postreply/(?P<post_id>\d+)/(?P<max_reply_id>\d+)$', 'discussion.views.get_postreply', name = 'get_postreply'),
    url(r'^discussion_reply/delete_post/(?P<post_id>\d+)$', 'discussion.views.delete_post', name = 'delete_post'),
    url(r'^discussion_reply/delete_reply/(?P<reply_id>\d+)$', 'discussion.views.delete_reply', name  = 'delete_reply'),
    # url(r'^discussion_reply/get_postreply$', 'discussion.views.get_postreply', name = 'get_postreply'),
    # url(r'discussion_reply/get_postreply?'),
    url(r'^chat$','discussion.views.index',name ='chat'),
    url(r'^goRoom/(?P<room_id>\d+)$', 'discussion.views.room',name='room'),
    url(r'^getmsg/$', 'discussion.views.getmsg'),
    url(r'^putmsg/$', 'discussion.views.putmsg'),
    url(r'^exitchat/$', 'discussion.views.exituser'),
    url(r'^onlinelist/$', 'discussion.views.onlineuser'),
    url(r'^createRoom$', 'discussion.views.newRoom',name='createRoom'),
    url(r'^update/$', 'discussion.views.updateRoom'),
    url(r'^delete/(?P<rid>\d+)$','discussion.views.deleteRoom',name='deleteRoom'),
   ]
