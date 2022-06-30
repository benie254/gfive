from rest_framework import serializers
from .models import Book,Like,Comment 


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book 
        fields = ('id','title','author','description','publisher')
 
 
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like 
        fields = ('id','like','book','user')

        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment  
        fields = ('id','comment','book','user')
        
