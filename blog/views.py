
from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator
# Create your views here.


def  blogdetail(request, slug):
     blogdetail = Post.objects.get(slug=slug)
     context = {
        'post' : blogdetail
    }
     return render(request, 'blog/blogdetail.html', context)  
    



def  blog(request):

    blog_liste = Post.objects.all()
    paginator = Paginator(blog_liste, 2) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'category': Category.objects.all(),
        'posts': page_obj,
       
    }
    return render(request, 'blog/blog.html', context )  