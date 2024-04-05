from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
    


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)  

    def __str__(self) -> str:
        return self.title