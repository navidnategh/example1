from . import views
from django.urls import path

app_name = "articles"

urlpatterns = [
    path   ('',  views.articles_list ,name='list') ,

    path ('creat', views.creat_article, name = 'creat' ) ,

    path ('<slug>' , views.article_detail, name='details'),
]
