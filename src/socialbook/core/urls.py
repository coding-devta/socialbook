from django.urls import path
from .views import *

urlpatterns =[
    path('' , home , name =  "home"),
    path('signup',  signup , name= "signup"),
    path('signin',  signin , name= "signin"),
    path('logout',  logout , name= "logout"),
    path('settings',  settings , name= "settings"),
    path('upload',  upload , name= "upload"),
    path('like-post',  like_post , name= "like-post"),
    path('profile',  profile , name= "profile"),
]