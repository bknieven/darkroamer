from django.db import models

# Create your models here.
class ArticleQuerySet(models.QuerySet):
    def published(self):
        return self.filter(is_publish=True)

class Tag(models.Model):
    slug = slug = models.SlugField(max_length=200,unique=True)

    def __str__(self):
        return self.slug

class Article(models.Model):
    title_text = models.CharField(max_length=200,default="")
    #title_word = models.CharField(max_length=100,default="")	#used in url
    slug = models.SlugField(max_length=200,unique=True)
    #slug = models.CharField(max_length=100,default="")
    article_text = models.TextField(default="")
    pub_date = models.DateTimeField('article published')    #'article published' is displayed in the admin page when edit one article
    mod_date = models.DateTimeField('article modified', auto_now=True)
    is_publish = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag)
    objects = ArticleQuerySet.as_manager()

    def __str__(self):
        return self.title_text

    class Meta:
        verbose_name = "Blog Article"
        verbose_name_plural = "Blog Articles"
        ordering = ["-pub_date"]

class Note(models.Model):
    note_text = models.TextField(default="")
    note_email = models.TextField(default="")
    pub_date = models.DateTimeField('note published')

class About(models.Model):
    about_text = models.TextField(default="")
