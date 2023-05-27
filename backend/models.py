from django.db import models

class ManyCategory(models.Model):
    category = models.CharField(max_length=255)
    types = models.CharField(max_length=255)

    def __str__(self):
        return  self.category
    
    
class ManyTags(models.Model):
    tags = models.CharField(max_length=255)

    def __str__(self):
        return  self.tags    
    
class ManyBrowzers(models.Model):
    browzers = models.CharField(max_length=255)

    def __str__(self):
        return  self.browzers   

class Manylanguages(models.Model):
    languages = models.CharField(max_length=255)

    def __str__(self):
        return  self.languages        


class Post(models.Model):
    name = models.CharField(max_length=255)
    date1 = models.DateField(auto_now_add=False)
    username = models.CharField(max_length=255)
    img = models.ImageField(upload_to='img/', default='img/img.jpg', null=True, blank= True)
    down = models.FileField(upload_to='media')
    life = models.CharField(max_length=255)
    category = models.ForeignKey(ManyCategory, on_delete=models.CASCADE)
    tags = models.ManyToManyField(ManyTags, blank=True)
    resolution = models.BooleanField(default=False)
    browsers = models.ManyToManyField(ManyBrowzers, blank=True)
    date2 = models.DateField(auto_now=False)
    github = models.CharField(max_length=255)
    languages = models.ManyToManyField(Manylanguages, blank=True)
    layout = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True)


    def __str__(self):
        return self.name
    
class Turi(models.Model):
    languages = models.CharField(max_length=255)
    
    def __str__(self):
        return  self.languages

class Menu(models.Model):
    name = models.CharField(max_length=255)
    languages  = models.ForeignKey(Turi, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255,unique=True)
    

    def __str__(self):
        return  self.name

    