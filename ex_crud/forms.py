#coding=utf8
from django import forms

class ArticleWriteForm(forms.Form):
	title = forms.CharField(
		label="제목",
		widget = forms.TextInput(attrs={'size': 64})
	)
	text = forms.CharField(
		label="내용",
		widget = forms.Textarea
	)
	user = forms.IntegerField(
		label="글쓴이",
		widget = forms.HiddenInput(attrs={'value': 1})
	)