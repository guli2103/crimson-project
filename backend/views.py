from django.shortcuts import render
from .models import Post
import os
from django.http import HttpResponse
from django.http import Http404
from django.conf import settings
from django.db.models import Q
from .models import Post, Menu, Turi , ManyCategory
from django.core.paginator import Paginator


def index(request):
    posts = Post.objects.all().order_by('-id').count() 
    posts1 = Menu.objects.all()
    posts2 = Turi.objects.all()
    categories = ManyCategory.objects.all()

    category = request.GET.get('category')

    if category == None:
    
        if 'q' in request.GET:
            q = request.GET['q']
            post =  Q(Q(name__icontains=q)|Q(username__icontains=q)|Q(category__category__icontains=q))
            posts = Post.objects.filter(post)
            count = Post.objects.all().filter(post).count()
        else:
            posts = Post.objects.all().order_by("-date1")
            count = Post.objects.all().order_by("-date1").count()
    else:
        if 'q' in request.GET:
            q = request.GET['q']
            post =  Q(Q(name__icontains=q)|Q(username__icontains=q)|Q(category__category__icontains=q))
            posts = Post.objects.filter(post)
            count = Post.objects.all().order_by("-date1").count()
        else:
            posts = Post.objects.filter(category__category = category )
            count = Post.objects.all().order_by("-date1").count()        
    paginator = Paginator(posts, 2 ) 
    page_number = request.GET.get('page', 1)
    project_pagination = paginator.get_page(page_number)
    totalpages = project_pagination.paginator.num_pages
    page_range = paginator.get_elided_page_range(number=page_number)   
 
    context = {
        'posts' : project_pagination,
        'totalpages' : totalpages,
        'list_pagination' : [n+1 for n in range(totalpages)],
        'page_range' : page_range,
        'posts1' : posts1 ,
        'posts2' : posts2,
        'categories' : categories,
        'category' : category,
        'count' : count,
        
    }   

    return render(request, 'index.html', context)

def index1(request):
    posts = Post.objects.all().order_by('-id').count() 
    posts1 = Menu.objects.all()
    posts2 = Turi.objects.all()
    categories = ManyCategory.objects.all()

    category = request.GET.get('category')

    if category == None:
    
        if 'q' in request.GET:
            q = request.GET['q']
            post =  Q(Q(name__icontains=q)|Q(username__icontains=q)|Q(category__category__icontains=q))
            posts = Post.objects.filter(post)
            count = Post.objects.all().filter(post).count()
        else:
            posts = Post.objects.all().order_by("-date1")
            count = Post.objects.all().order_by("-date1").count()
    else:
        if 'q' in request.GET:
            q = request.GET['q']
            post =  Q(Q(name__icontains=q)|Q(username__icontains=q)|Q(category__category__icontains=q))
            posts = Post.objects.filter(post)
            count = Post.objects.filter(post).count()
        else:
            posts = Post.objects.filter(category__category = category )
            count = Post.objects.filter(category__category = category ).count()        
    paginator = Paginator(posts, 1 ) 
    page_number = request.GET.get('page', 1)
    project_pagination = paginator.get_page(page_number)
    totalpages = project_pagination.paginator.num_pages
    page_range = paginator.get_elided_page_range(number=page_number)   
 
    context = {
        'posts' : project_pagination,
        'totalpages' : totalpages,
        'list_pagination' : [n+1 for n in range(totalpages)],
        'page_range' : page_range,
        'posts1' : posts1 ,
        'posts2' : posts2,
        'categories' : categories,
        'category' : category,
        'count' : count,
        
    }   

    return render(request, 'index.html',context )

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
    return render(request, 'category.html')


def details(request, slug ):
    top = Post.objects.get(slug=slug)
    posts = Post.objects.all().order_by('?')[:3]
    context = {
        'top' :top,
        'posts' :posts 
    } 
    return render(request, 'details.html', context)


def shop(request ):
    post3 = Post.objects.all()
    posts1 = Menu.objects.all()
    yangi = Menu.objects.all()
    posts2 = Turi.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        post =  Q(Q(name__icontains=q)|Q(username__icontains=q)|Q(category__category__icontains=q))
        post3 = Post.objects.filter(post)
    else:
        post3 = Post.objects.all()
    paginator = Paginator(post3, 3 ) 
    page_number = request.GET.get('page', 1)
    project_pagination = paginator.get_page(page_number)
    totalpages = project_pagination.paginator.num_pages
    page_range = paginator.get_elided_page_range(number=page_number) 
    
    post_filter = Post.objects.filter(category=post3)

    context = {
        'post3' : project_pagination,
        'totalpages' : totalpages,
        'list_pagination' : [n+1 for n in range(totalpages)],
        'page_range' : page_range,
        'posts1' : posts1 ,
        'posts2' : posts2,
        'yangi'  : yangi ,
        ' post_filter ' :  post_filter 
    } 

    return render(request, 'shop.html', context)





