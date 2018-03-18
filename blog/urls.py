from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='blog_page'),
    url(r'^(?P<title_word>[0-9a-zA-Z\_]+)/$', views.article_page, name='article_page'),
]
