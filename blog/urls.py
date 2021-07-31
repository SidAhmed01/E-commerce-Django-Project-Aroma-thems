from django.urls import path 
from . import views




app_name = 'blogs'


urlpatterns = [
    path('<slug:slug>', views.blogdetail, name='blogdetail'),
    path('', views.blog, name='blog'),
]