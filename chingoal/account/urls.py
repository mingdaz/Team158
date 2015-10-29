
from django.conf.urls import include, url

urlpatterns = [
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'account/login.html'}),
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login', name = 'logout'),
    url(r'^register$', 'account.views.register', name = 'register'),
    url(r'^edit-profile$', 'account.views.edit_profile', name= 'editProfile'),
    url(r'^view-profile/(?P<uname>\w+)$', 'account.views.view_profile', name = 'viewProfile'),
    url(r'^reset-password$', 'account.views.reset_password', name = 'resetPassword'),
    url(r'^new-password/(?P<token>.*)$', 'account.views.new_password', name = 'newPassword'),
    url(r'^edit-schedule$', 'account.views.edit_schedule', name= 'editSchedule'),
    url(r'^add-follower/(?P<uname>\w+)$', 'account.views.add_follower', name = 'addFollower'),
    url(r'^remove-follower/(?P<uname>\w+)$', 'account.views.remove_follower', name = 'removeFollower'),
]
