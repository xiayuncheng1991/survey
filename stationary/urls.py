from django.conf.urls import patterns, include, url
from django.contrib import admin

from stationary import views


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'survey.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name="index"), 
    url(r'^result/$', views.result, name="result"),
    url(r'^json_stationarytype/$', views.get_stationarytype_json, name="json_stationarytype"),
)
