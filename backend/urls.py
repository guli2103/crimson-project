from django.urls import path
from .views import *



urlpatterns = [
    path('', index ),
    path('about/', about , name='about'),
    path('404/', xato404, name='404'),
    path('about-p/', about_p , name='about_p'),
    path('category/', category, name='category'),
]
