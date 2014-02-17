from django.conf.urls import patterns, url
from trades import views

urlpatterns = patterns('',
    # ex: /trades/
    url(r'^$', views.index, name='index'),
    # ex: /trades/5/
    url(r'^(?P<trade_id>\d+)/$', views.detail, name='detail'),
    # ex: /trades/5/results/

)
