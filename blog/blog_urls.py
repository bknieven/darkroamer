from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='blog_homepage'),
    url(r'^(?P<page_num>\d+)/$',views.homepage,name='blog_page'),
    url(r'^(?P<slug>[0-9a-zA-Z\_\-]+)/$', views.article_page, name='article_page'),
]
