
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', '../home.views.home',name = 'home'),
    url(r'^edit-profile$', '../account.views.edit_profile', name = 'editProfile' ),
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login', name = 'logout'),
]
