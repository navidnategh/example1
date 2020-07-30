from django.shortcuts import render
from . import models

# Create your views here.

def articles_list(request) :

    articles = models.Article.objects.all().order_by('date')
    arg = { 'articles': articles }

    return render(request, 'articles/articles_list.html',arg)
