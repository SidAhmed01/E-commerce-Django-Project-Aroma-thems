from django.urls import path
from . import views

app_name = 'path'
urlpatterns = [

      path('',  views.login, name ='login'),
      path('register/', views.register, name='register'),
      path('forgetpassword/', views.forgetpassword, name='forgetpassword'),
      path('resetpassword/', views.resetpassword, name='resetpassword'),
      path('confermationpassword/', views.confermationpassword, name='confermationpassword'),
      path('password_reset_confirm/', views.password_reset_confirm, name='password_reset_confirm'),
      
      path('logout/', views.logged_out, name='logged_out'),
      path('profile/', views.profile, name='profile'),
      path('update/', views.updateprofile, name='update'),


]