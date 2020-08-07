from django.shortcuts import render
from . import models
from django.shortcuts import HttpResponse

from django.contrib.auth.decorators import login_required

# Create your views here.

def articles_list(request) :

    articles = models.Article.objects.all().order_by('-date')
    arg = { 'articles': articles }

    return render(request, 'articles/articles_list.html',arg)


def article_detail (request , slug ) :
     # return HttpResponse (slug)
     article = models.Article.objects.get(slug=slug)

     return render (request , 'articles/article_detail.html',{'article':article})



@login_required(login_url='/accounts/login')
def creat_article(request) :
    return render (request, 'articles/creat_article.html')
