from django.contrib import admin

# Register your models here.
from . import models


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title_text","pub_date",'is_publish')
    prepopulated_fields = {"slug":("title_text",)}

#admin.site.register(Article)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Note)
admin.site.register(models.Tag)
admin.site.register(models.About)
