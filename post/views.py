from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from post.serializer import BookSerializer,LikeSerializer,CommentSerializer
from post.models import Book,Like,Comment 
from rest_framework import status
from .permissions import IsAdminOrReadOnly

# Create your views here.
class OurBookLibrary(APIView):
    def get(self,request,format=None):
        books = Book.objects.all()
        serializers = BookSerializer(books,many=True)
        return Response(serializers.data)

    def post(self,request,format=None):
        permission_classes = (IsAdminOrReadOnly,)
        serializers = BookSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    

class Comments(APIView):
    def get(self,request,pk,format=None):
        comments = Comment.objects.all().filter(book_id=pk)
        serializers = CommentSerializer(comments,many=True)
        return Response(serializers.data)

    def post(self,request,format=None):
        permission_classes = (IsAdminOrReadOnly,)
        serializers = CommentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    

class Likes(APIView):
    def get(self,request,pk,format=None):
        likes = Like.objects.all().filter(book_id=pk)
        serializers = LikeSerializer(likes,many=True)
        return Response(serializers.data)

    def post(self,request,pk,format=None):
        permission_classes = (IsAdminOrReadOnly,)
        serializers = LikeSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)