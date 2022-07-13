from rest_framework import serializers
from .models import Book,Rating,Comment 
from .models import User,Profile 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile   
        fields = ('id','user','profile_picture','bio','name','phone_number','email')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book 
        fields = ('id','image','title','category','author','description','publisher','price')
 
 
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating 
        fields = ('id','rating_enjoyment','rating_recommend','rating_purchase','book','user')

        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment  
        fields = ('id','comment','book','user')
        
