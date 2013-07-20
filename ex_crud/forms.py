#coding=utf8
from django import forms
from django.core.urlresolvers import reverse
from django.db import models

from .models import T_article

class Article(models.Model):
	title = forms.TextInput(attrs={'size': 64})
	text = forms.Textarea
	written = forms.HiddenInput
	
	# On Python 3: def __str__(self):
	def __unicode__(self):
		return self.name

class ArticleWriteForm(forms.ModelForm):
	class Meta:
		model = T_article
		fields = ['title', 'text']