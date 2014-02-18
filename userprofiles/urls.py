from django.conf.urls import patterns, url
from userprofiles import views

urlpatterns = patterns('',
    url(r'^/(?P<slug>\w+)/$', views.UserProfileDetailView.as_view(), name='profile'),
)
