"""webapps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'basic.user_manage.home'),
    url(r'^register$', 'basic.user_manage.register', name = 'register'),
    url(r'^login$', 'django.contrib.auth.user_manage.login', {'template_name':'login.html'}),
    url(r'^logout$', 'django.contrib.auth.user_manage.logout_then_login', name = 'logout'),
    url(r'^edit-profile$', 'basic.user_manage.edit_profile', name= 'editProfile', name = 'editProfile'),
    url(r'^view-profile/(?P<uname>\w+)$', 'basic.user_manage.view_profile', name = 'viewProfile'),
    url(r'^reset-password$', 'basic.user_manage.reset_password', name = 'resetPassword'),
    url(r'^new-password/(?P<token>.*)$', 'basic.user_manage.new_password', name = 'newPassword'),
    url(r'^edit-schedule$', 'basic.user_manage.edit_schedule', name= 'editSchedule'),
    url(r'^add-follower/(?P<uname>\w+)$', 'basic.user_manage.add_follower', name = 'addFollower'),
    url(r'^remove-follower/(?P<uname>\w+)$', 'basic.user_manage.remove_follower', name = 'removeFollower'),
]