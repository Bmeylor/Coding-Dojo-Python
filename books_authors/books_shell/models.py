from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(max_length=200,default='Good Book')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book, related_name ="authors")
    notes = models.TextField(max_length=200,default='random notes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
