import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify
# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(User, related_name='post_author', on_delete=models.CASCADE)
    title= models.CharField(max_length=200)
    tags = TaggableManager()
    images=models.ImageField(upload_to='post/')
    created_at=models.DateTimeField(default=datetime.datetime.now)
    description=models.TextField(max_length=500)
    category=models.ForeignKey('Category', related_name='post_category', on_delete=models.CASCADE)
    sllug=models.SlugField(null=True,blank=True) 
    def save(self, *args, **kwargs):
       if not self.sllug:
           self.sllug=slugify(self.title)
           
       super(Post, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
       return self.name
 

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
     