from django.conf.urls import patterns, include, url
from django.contrib import admin

from survey import settings


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'survey.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/archive/', include('archive.urls',namespace='archive')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^stationary/', include('stationary.urls',namespace='stationary')),
    url(r'^account/', include('account.urls',namespace='account')),
#     url(r'^(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
)
