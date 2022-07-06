from rest_framework import serializers
from .models import Book,Rating,Comment,Category 


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = ('id','category')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book 
        fields = ('id','title','author','description','publisher')
 
 
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating 
        fields = ('id','rating','book','user')

        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment  
        fields = ('id','comment','book','user')
        
