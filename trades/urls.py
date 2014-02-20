from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from trades import views

urlpatterns = patterns('',

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^new$', login_required(views.CreateView.as_view()), name="new_trade"),
)
