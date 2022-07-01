from django.db import models
from django.contrib.auth.models import User 
from cloudinary.models import CloudinaryField

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    description = models.CharField(max_length=120)
    publisher = models.CharField(max_length=120)
    image = CloudinaryField('Featured image',null=True)
    
class Rating(models.Model):
    rating = models.PositiveIntegerField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    book = models.ForeignKey(Book,on_delete=models.CASCADE,null=True)
  
    
class Comment(models.Model):
    comment = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    book = models.ForeignKey(Book,on_delete=models.CASCADE,null=True)
    
    

    
