from unicodedata import name
from django.urls import path
from . import views
from .views import *



urlpatterns=[
    path('login/',login_page ,name='login'),
    path('',index,name='index'),
    path('dash/',dash,name='dash'),
    path('logout/',logout_user, name='logout'),
    path('signup/',signup_page, name='signup'),
    path('cours/upload/', cour_upload, name='cour_upload'),
    path('cours/', cours, name='cours'),
    path('devoirs/', all_devoir, name='devoirs'),
    path('coursInfo/', coursInfo, name='coursInfo'),

   
]