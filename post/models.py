from django.db import models
from django.contrib.auth.models import User,AbstractUser
from cloudinary.models import CloudinaryField
from pytz import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    # username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = CloudinaryField('Profile photo',null=True)
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    phone_number = models.CharField(blank=True, max_length=120)
    email = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save

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
    
    

    
