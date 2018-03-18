from django.core.urlresolvers import reverse
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import resolve
from .models import Article
from .views import article_page
from . import blog_urls

class ArticleFeed(Feed):
    title = "DarkRoamer's blog"
    link = "http://127.0.0.1:8000/blog/"
    description = "Feed of DarkRoamer's blog"

    def items(self):
        return Article.objects.published()[0:5]

    def item_title(self, item):
        return item.title_text

    def item_description(self, item):
        return item.article_text
    
    def item_link(self, item):
        return '/blog'+reverse(article_page,kwargs={'slug': item.slug},urlconf=blog_urls) #The default urlconf is url.py in root dir.If we use the url in another urlconf module ,we must set the urlconf parameter.
#I don't kown how to let reverse() return /blog/xxx/,so I just add "/blog" to the return path manually.
