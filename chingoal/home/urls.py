
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'home.views.home'),
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login', name = 'logout'),
]
