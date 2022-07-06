from rest_framework import serializers
from .models import Book,Rating,Comment 


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book 
        fields = ('id','image','title','category','author','description','publisher','price')
 
 
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating 
        fields = ('id','rating','book','user')

        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment  
        fields = ('id','comment','book','user')
        
