
from django.conf.urls import include, url

urlpatterns = [
    url(r'^buy-title$', 'store.views.buy_title', name= 'buyTitle'),
    url(r'^unlock-learning$', 'store.views.unlock_learning', name= 'unlockLearning'),
    url(r'^earn-money$', 'store.views.earn_money', name= 'earnMoney'),
]
