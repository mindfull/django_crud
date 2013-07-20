#coding=utf8

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.db.models import F

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
	articles = T_article.objects.order_by('-id')
	
	variables = Context({
		'page_title': 'List',
		'articles': articles
	})
	output = render(request,'list.html',variables)
	return HttpResponse(output)

# def Write(request):
# 	if request.method=='POST':
# 		form = ArticleWriteForm(request.POST)
# 		if form.is_valid():
# 			article = T_article.objects.create(
# 				title=form.cleaned_data['title'],
# 				text = form.cleaned_data['text'],
# 				user = User.objects.get(id=1),
# 				written = datetime.datetime.now()
# 			)
# 			
# 			article.save()
# 			return HttpResponseRedirect(
# 				'/'
# 			)
# 			
# 	else:
# 		form = ArticleWriteForm()
# 	
# 	variables = Context({
# 		'page_title': 'Write',
# 		'articleForm': form
# 	})
# 	output = render(request,'write.html',variables)
# 	return HttpResponse(output)

class ArticleCreateView(CreateView):
	model = Article
	form_class = ArticleWriteForm
	success_url = '/'
	template_name = "write.html"
	
	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.written = datetime.datetime.now()
		return super(ArticleCreateView, self).form_valid(form)


def View(request, postid):
	article = get_object_or_404(T_article, id=postid)
	T_article.objects.filter(id=postid).update(readcount=F('readcount')+1)
	
	variables = Context({
		'page_title': 'View',
		'article': article
	})
	output = render(request,'view.html',variables)
	return HttpResponse(output)

# def Modify(request, postid):	
# 	article = get_object_or_404(T_article, id=postid)
# 	if request.method=='POST':
# 		form = ArticleWriteForm(request.POST)
# 		if form.is_valid():
# 			article.title=form.cleaned_data['title']
# 			article.text = form.cleaned_data['text']
# 			article.modified = datetime.datetime.now()
# 			article.save()
# 			return HttpResponseRedirect(
# 				'/'
# 			)
# 	
# 	else:
# 		form = ArticleWriteForm(request.POST, instance=article)
# 		form.title = article.title
# 		form.text = article.text
# 	
# 	variables = Context({
# 		'page_title': 'Modify',
# 		'articleForm': form
# 	})
# 	output = render(request,'modify.html',variables)
# 	return HttpResponse(output)
	
def Delete(request, postid):
	article = get_object_or_404(T_article, id=postid)
	T_article.objects.filter(id=postid).update(readcount=F('readcount')+1)
	
	variables = Context({
		'page_title': 'View',
		'article': article
	})
	output = render(request,'view.html',variables)
	return HttpResponse(output)