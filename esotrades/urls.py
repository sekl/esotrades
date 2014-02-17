from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'esotrades.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'trades/', include('trades.urls', namespace='trades')),
    url(r'^admin/', include(admin.site.urls)),
)
