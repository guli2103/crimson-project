from django.contrib import admin
from .models import ManyBrowzers, ManyCategory, Manylanguages, ManyTags, Post,Turi,Menu  


admin.site.register((Post, ManyCategory, ManyBrowzers, ManyTags, Manylanguages, Turi, Menu ))


