from django.conf.urls import patterns, include, url
from ex_crud.views import *
from ex_crud import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', List),
	url(r'^Write/$', views.ArticleCreateView.as_view(), name='article_create'),
	url(r'^Modify/(?P<id>\d+)/$', views.ArticleUpdateView.as_view(), name='article_update'),
	#(r'^Modify/(\d)/$', Modify),
	(r'^View/(\d+)/$', View),
	(r'^Login/$', 'django.contrib.auth.views.login'),
	url(r'^Delete/(?P<id>\d+)/$', views.ArticleDeleteView.as_view(), name='article_delete')
)
