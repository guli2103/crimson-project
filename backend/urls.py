from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static 
from django.urls import  re_path as url
from django.views.static import serve


urlpatterns = [
    path('', index ),
    url(r'^download/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),


    path('about/', about , name='about'),
    path('404/', xato404, name='404'),
    path('about-p/', about_p , name='about_p'),
    path('categoryy/', category, name='category'),
    path('details/<slug:slug>', details, name='details'),
    path('shop/', shop, name='shop'),  
    path('index1/', index1, name='index1')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
