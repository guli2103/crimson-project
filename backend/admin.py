from django.contrib import admin
from .models import ManyBrowzers, ManyCategory, Manylanguages, ManyTags, Post


admin.site.register((Post, ManyCategory, ManyBrowzers, ManyTags, Manylanguages))


