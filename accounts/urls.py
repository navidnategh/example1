from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns =[

    path ('signup' , views.signup_view , name = 'signup') ,

    path ('' , views.signup_view , name = 'accounts') ,



]
