from django.conf.urls import patterns, include, url
from django.contrib import admin

from archive import views


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'survey.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^stationaryarchive/$', views.stationary_index, name="stationary_archive_index"),
    url(r'^archive_stationary/$', views.archive_stationary, name="archive_stationary"),
    url(r'^json_stationaryarchive/$', views.get_stationaryarchive_json, name="json_stationaryarchive"),
   
)
