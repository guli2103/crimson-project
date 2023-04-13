from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


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





