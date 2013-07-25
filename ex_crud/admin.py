from django.contrib import admin
from ex_crud.models import T_article, T_comment, T_file

class AdminBookmark (admin.ModelAdmin) :
	list_display = ("link", )

admin.site.register(T_article, )
admin.site.register(T_comment, )
admin.site.register(T_file, )