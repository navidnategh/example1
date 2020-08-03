from django.db import models

# Create your models here.
class Article (models.Model) :
    title = models.CharField (max_length = 30)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField( auto_now_add = True )
    image = models.ImageField(default = 'default' , blank = True)


    def __str__(self):
        return self.title

    def str (self) :
        return self.title


    def snipper(self) :
        return self.body[ 0 :  80 ] + ' ...'
