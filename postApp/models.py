from django.db import models

# Create your models here.
class Book(models.Model):
    author = models.CharField(max_length=60)
    description = models.CharField(max_length=60)