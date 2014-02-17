from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('home.urls', namespace='home')),
    url(r'trades/', include('trades.urls', namespace='trades')),
    url(r'^admin/', include(admin.site.urls)),

)
