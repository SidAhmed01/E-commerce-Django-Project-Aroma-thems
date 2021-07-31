from django.urls import path 
from . import views


app_name = 'productspage'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('shopcategory/', views.shopcategory, name='shopcategory'),
    path('<slug:slug>', views.productdetails, name='productdetails'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('shopingcart/', views.shopingcart, name='shopingcart'),
    path('productcheckout/', views.productcheckout, name='productcheckout'),
]
