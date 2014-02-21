from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('pages.urls', namespace='pages')),
    url(r'^search/', include('haystack.urls')),
    url(r'^trades/', include('trades.urls', namespace='trades')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/profile', include('userprofiles.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
)
