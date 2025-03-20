from django.contrib import admin
from django.db import models
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    born = models.DateField()
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    perex = models.TextField()
    link = models.URLField()
    published_date = models.DateField()
    date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)