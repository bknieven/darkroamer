from django.shortcuts import render,get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
from .models import Article
from .models import Note
from .models import About

article_num_one_page = 5   #the number of articles displayed in main page
abstract_length = 600  #the byte of abstract text

def homepage(request,page_num=1):
    all_articles = Article.objects.published()  #filter out articles whose is_publish is ture.
    p = Paginator(all_articles, article_num_one_page)
    articles_this_page = p.page(page_num)

    for article in articles_this_page:
        if(len(article.article_text) > abstract_length):
            article.abstract = article.article_text[:abstract_length]
            article.isabstract = True   #whether the abstract text not contains all the article
        else:
            article.abstract = article.article_text
            article.isabstract = False
    context = {
        'articles_this_page': articles_this_page
    }
    return render(request, 'blog/homepage.html', context)

def article_page(request,slug):
    article = get_object_or_404(Article,slug=slug)
    context = {
        'article':article
    }
    return render(request, 'blog/article_page.html',context)

def note_page(request):
    latest_note_list = Note.objects.order_by('-pub_date')
    context = {
        'latest_note_list': latest_note_list,
    }
    return render(request, 'blog/note.html', context)

def archive_page(request):
    all_articles = Article.objects.published()  #filter out articles whose is_publish is ture.
    #for article in all_articles:
    context = {
        'all_articles': all_articles
    }
    return render(request, 'blog/archive_page.html', context)

def about_page(request):
    about = About.objects.all()[0]
    #about_text = get_object_or_404(About,slug=slug)
    context = {
        'about': about
    }
    return render(request, 'blog/about_page.html', context)

def add_note(request):
    try:
        text_get = request.POST['note_textarea']
        email_get = request.POST['note_emailarea']
        if (len(text_get) == 0):
            latest_note_list = Note.objects.order_by('-pub_date')
            context = {
                'latest_note_list': latest_note_list,
                'error_message': "输入内容为空",
            }
            return render(request, 'blog/note.html', context)
        note_added = Note(note_text=text_get,note_email=email_get,pub_date=timezone.now())
    except (KeyError,Note.DoesNotExist):
        return HttpResponseRedirect(reverse('note_page'))#temp
    else:
        note_added.save()
        return HttpResponseRedirect(reverse('note_page'))
