
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'store.views.home', name= 'store'),
    url(r'^buy-title/(?P<title>\w+)$', 'store.views.buy_title', name= 'buyTitle'),
    url(r'^unlock-learning/(?P<lesson>\w+)$', 'store.views.unlock_learning', name= 'unlockLearning'),
    url(r'^earn-money$', 'store.views.earn_money', name= 'earnMoney'),
]
