from django.urls import path
from .views import *

app_name='webpage'

urlpatterns=[
    path('',home,name='home'),
    path('course/',course,name='course'),
    path('bootcamp/',bootcamp,name='bootcamp'),
    path('callback/',callback,name='callback'),
    path('signin/',signin,name='signin')

]