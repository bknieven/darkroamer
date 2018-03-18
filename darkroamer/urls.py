"""darkroamer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from blog import views,feed

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^blog/', include('blog.blog_urls',namespace='blog')),
    url(r'^feed/$',feed.ArticleFeed(),name='feed'),
    url(r'^archive/$',views.archive_page,name='archive_page'),
    url(r'^about/$',views.about_page,name='about_page'),
	#namespace is used in template files.e.g.{% url 'blog:article_page' article.title_word %}
    url(r'^admin/', admin.site.urls),
    url(r'^note/$',views.note_page,name='note_page'),
    url(r'^note/addnote/$',views.add_note,name='add_note'),
]
