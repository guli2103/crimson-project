from django.shortcuts import render
from .models import Post
import os
from django.http import HttpResponse
from django.http import Http404
from django.conf import settings
from django.db.models import Q
from .models import Post


def index(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'index.html', context)


def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response = HttpResponse(fh.read(), content_type='backend/down')
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
        
    raise Http404    

def about(request):
    return render(request, 'about.html')


def xato404(request):
    return render(request, '404.html')

def about_p(request):
    return render(request, 'about-p.html')

def category(request):
    return render(request, 'detail-category.html')


def details(request): 
    return render(request, 'details.html')


def shop(request):
    return render(request, 'shop.html')





