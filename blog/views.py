from django.urls import path
from django.shortcuts import render
from . import urls



def home (request) :
    return render(request,'home.html')


def about(request) :
    return render (request, 'about.html')
