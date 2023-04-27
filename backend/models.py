from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=False)
    username = models.CharField(max_length=255)
    img = models.ImageField(upload_to='img/', default='img/moychechal.jpg', null=True, blank= True)


    def __str__(self):
        return self.username
    

class TopPost(models.Model):
    life = models.CharField(max_length=255)
    