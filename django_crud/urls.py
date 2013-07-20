from django.conf.urls import patterns, include, url
from ex_crud.views import *
from ex_crud import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', List),
	(r'^Write/$', views.ArticleCreateView.as_view()),
	#(r'^Modify/(\d)/$', Modify),
	(r'^View/(\d)/$', View),
	(r'^Login/$', 'django.contrib.auth.views.login'),
	(r'^Delete/(\d)/$', Delete)
)
