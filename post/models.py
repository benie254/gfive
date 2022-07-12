from django.db import models
from django.contrib.auth.models import User,AbstractUser
from cloudinary.models import CloudinaryField

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Book(models.Model):
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    category = models.CharField(max_length=60,null=True)
    description = models.CharField(max_length=120)
    publisher = models.CharField(max_length=120)
    image = CloudinaryField('Featured image',null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return str(self.item) + ": Ksh" + str(self.price)
    
class Rating(models.Model):
    rating_enjoyment = models.PositiveIntegerField(null=True)
    rating_recommend = models.PositiveIntegerField(null=True)
    rating_purchase = models.PositiveIntegerField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    book = models.ForeignKey(Book,on_delete=models.CASCADE,null=True)
  
    
class Comment(models.Model):
    comment = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    book = models.ForeignKey(Book,on_delete=models.CASCADE,null=True)
    
    

    
