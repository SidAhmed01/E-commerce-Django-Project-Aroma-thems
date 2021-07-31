from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
# Create your views here.
from .models import * 
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib import messages
from django.contrib import auth



#start_login_object
def  login(request):


    if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:

                    dj_login(request, user)
                    return redirect('productspage:index')
                else:

                    messages.info(request, 'Username OR Password is incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)



    

#end_login_object
#_____________



#start_register_object
def  register(request):



    form = CreateUserForm()
    if request.method == 'POST':

        form = CreateUserForm(request.POST)
    if form.is_valid():

        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, 'Account was created for ' + user)
        return redirect('path:login')
    context = {'form':form}
    return render(request, 'accounts/register.html', context)
    
        
 

#end_register_object
#_____________

#start_logout_object
def  logged_out(request):
    auth.logout(request)

    
    return render(request, 'accounts/logged_out.html') 

        
    

  

#end_logout_object
#_____________

def  forgetpassword(request):
    return render(request, 'accounts/password_reset_email.html')  


def resetpassword (request):
    return render(request, 'accounts/password_reset_form.html')

def  confermationpassword(request):
    return render(request, 'accounts/password_reset_done.html')



def  confermationpassword(request):
    return render(request, 'accounts/password_reset_complete.html')


def  password_reset_confirm(request):
    return render(request, 'accounts/password_reset_confirm.html')



def  profile(request):
    context = {}
    return render(request, 'accounts/profile.html')



def  updateprofile(request):
    return render(request, 'accounts/update.html')