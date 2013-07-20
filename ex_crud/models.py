from django.db import models
from django.contrib.auth.models import User

class T_article(models.Model):
	title = models.CharField(max_length=200)
	user = models.ForeignKey(User, default=1)
	text = models.TextField()
	written = models.DateTimeField()
	modified = models.DateTimeField(null=True)
	comments = models.IntegerField(default=0)
	readcount = models.IntegerField(default=0)
	
class T_comment(models.Model):
	user = models.ForeignKey(User, default=1)
	article = models.ForeignKey(T_article)
	text = models.TextField()
	written = models.DateTimeField()
	modified = models.DateTimeField(null=True)
