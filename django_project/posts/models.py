from django.db import models

# Create your models here.
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length = 50)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.title