from email import contentmanager
from pyexpat import model
from turtle import title
from django.db import models
from django.forms import CharField

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #auth


    def __str__(self):
        return f'[{self.pk}] {self.title}'