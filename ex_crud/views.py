#coding=utf8

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.db.models import F

from django.core.paginator import Paginator, InvalidPage, EmptyPage

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from ex_crud.forms import *
import datetime

from .models import T_article, T_comment
import time

def __init__(self, *args, **kwargs):
	super(ex_crud, self).__init__(*args, **kwargs)
	self.fields['title'].label = "제목"
	self.fields['text'].label = "내용"

def List(request):
	if request.GET.get('per_page'):
		request.session['per_page'] = int(request.GET.get('per_page'))
	
	per_page = request.session.get('per_page', 10)
	
	query_set = T_article.objects.order_by('-id')
	paginator = Paginator(query_set, per_page)
	
	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1
		
	try:
		articles = paginator.page(page)
	except (EmptyPage, InvalidPage):
		articles = paginator.page(paginator.num_pages)
	
	variables = Context({
		'page_title': 'List',
		'articles': articles
	})
	return render(request,'list.html',variables)

class ArticleCreateView(CreateView):
	model = Article
	form_class = ArticleWriteForm
	success_url = '/'
	template_name = "write.html"
	
	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.written = datetime.datetime.now()
		return super(ArticleCreateView, self).form_valid(form)


class ArticleUpdateView(UpdateView):
	model = Article
	form_class = ArticleWriteForm
	success_url = '/'
	template_name = "modify.html"
	
	def get_object(self, queryset=None):
		obj = T_article.objects.get(id=self.kwargs['id'])
		return obj
	
	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.modified = datetime.datetime.now()
		return super(ArticleUpdateView, self).form_valid(form)


def View(request, postid):
	article = get_object_or_404(T_article, id=postid)
	T_article.objects.filter(id=postid).update(readcount=F('readcount')+1)
	
	variables = Context({
		'page_title': 'View',
		'article': article
	})
	output = render(request,'view.html',variables)
	return HttpResponse(output)

	
class ArticleDeleteView(DeleteView):
	model = Article
	success_url = '/'
	template_name = "delete.html"
	
	def get_object(self, queryset=None):
		obj = T_article.objects.get(id=self.kwargs['id'])
		return obj