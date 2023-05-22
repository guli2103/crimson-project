from django.contrib import admin
from .models import ManyBrowzers, ManyCategory, Manylanguages, ManyTags, Post,Turi,Menu  


admin.site.register((Post, ManyBrowzers, ManyTags, Manylanguages, Turi, Menu ,  ManyCategory ))


