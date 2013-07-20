#coding=utf8

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from ex_crud.forms import *
import datetime

from .models import T_article, T_comment
import time

def List(request):
	articles = T_article.objects.order_by('-id')
	
	variables = Context({
		'page_title': 'List',
		'articles': articles
	})
	output = render(request,'list.html',variables)
	return HttpResponse(output)

def Write(request):
	if request.method=='POST':
		form = ArticleWriteForm(request.POST)
		if form.is_valid():
			article = T_article.objects.create(
				title=form.cleaned_data['title'],
				text = form.cleaned_data['text'],
				user = User.objects.get(id=1),
				written = datetime.datetime.now()
			)
			
			article.save()
			return HttpResponseRedirect(
				'/'
			)
			
	else:
		form = ArticleWriteForm()
	
	variables = Context({
		'page_title': 'Write',
		'articleForm': form
	})
	output = render(request,'write.html',variables)
	return HttpResponse(output)

def View(request, postid):
	article = get_object_or_404(T_article, id=postid)
	
	variables = Context({
		'page_title': 'View',
		'article': article
	})
	output = render(request,'view.html',variables)
	return HttpResponse(output)

def Modify(reques, postid):
	try:
		user = T_article.object.get(id=postid)
	except:
		raise Http404('글이 존재하지 않습니다')
	
	variables = Context({
		'page_title': 'Modify'
	})
	output = render(request,'modify.html',variables)
	return HttpResponse(output)