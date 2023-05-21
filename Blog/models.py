from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(null=True,blank=True, upload_to="images/")
    
    def __str__(self) -> str:
        return self.title
    