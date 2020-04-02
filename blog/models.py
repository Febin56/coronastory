from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
 #   slug = models.SlugField(unique=True, blank=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='pictures/%Y/%m/', max_length=255, null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
  
    def __str__(self):
        return f'{self.title}'


    def total_likes(self):
        return self.likes.count()


    # def get_absolute_url(self):
    #     return reverse("blog:post_detail", args=[self.id, self.slug])

