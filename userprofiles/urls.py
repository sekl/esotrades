from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required as auth
from userprofiles import views

urlpatterns = patterns('',
    url(r'^/edit_profile/$', auth(views.UserProfileEditView.as_view()), name="edit_profile"),
    url(r'^/(?P<slug>\w+)/$', views.UserProfileDetailView.as_view(), name='profile'),
)
