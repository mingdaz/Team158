from django.conf.urls import include, url
from forms import MyAuthenticationForm

urlpatterns = [

    # url(r'^$', 'home.views.home'),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'account/new/login.html','authentication_form':MyAuthenticationForm},name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login', name = 'logout'),
    url(r'^register$', 'account.views.register', name = 'register'),
    url(r'^edit-profile$', 'account.views.edit_profile', name= 'editProfile'),
    url(r'^view-profile/(?P<uname>\w+)$', 'account.views.view_profile', name = 'viewProfile'),
    url(r'^reset-password$', 'account.views.reset_password', name = 'resetPassword'),
    url(r'^new-password/(?P<token>.*)$', 'account.views.new_password', name = 'newPassword'),
    url(r'^edit-schedule$', 'account.views.edit_schedule', name= 'editSchedule'),
    url(r'^follow/(?P<uname>\w+)/(?P<isFollowing>\w+)/(?P<isLearner>\w+)$', 'account.views.follow', name = 'follow'),
]
