from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator

# Create your views here.

#global_variable
 

def  index(request):
    context = {
    'product_list': Product.objects.all()

        
    }
    return render(request, 'pages/index.html', context)    


def  contact(request):
    return render(request, 'pages/contact.html')  


def  shopcategory(request):
    product_list = Product.objects.all()

    paginator = Paginator(product_list, 4) # Show 25 contacts per page.
    page = request.GET.get('page')
    product_list = paginator.get_page(page)
    context = {
    'product_list': product_list

        
    }



    return render(request, 'products/shopcategory.html', context)  


def  productdetails(request, slug):
    context = {
        'product_details' : Product.objects.get( slug = slug),
        
    }
    
    return render(request, 'products/productdetails.html', context)  


def  confirmation(request):
    return render(request, 'products/confirmation.html')  




def  shopingcart(request):
    return render(request, 'products/shopingcart.html')  




def  productcheckout(request):
    return render(request, 'products/productcheckout.html')  

