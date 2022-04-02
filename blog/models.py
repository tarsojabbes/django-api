from enum import auto
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

