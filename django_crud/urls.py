from django.conf.urls import patterns, include, url
from ex_crud.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', List),
	(r'^Write/$', Write),
	(r'^Modify/(\d)/$', Modify),
	(r'^View/(\w+)/$', View),
	(r'^Login/$', 'django.contrib.auth.views.login'),
)
