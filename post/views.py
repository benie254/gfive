from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from post.serializer import BookSerializer,RatingSerializer,CommentSerializer
from post.models import Book,Rating,Comment  
from rest_framework import status


# Create your views here.
class OurBookLibrary(APIView):
    def get(self,request,format=None):
        books = Book.objects.all()
        serializers = BookSerializer(books,many=True)
        return Response(serializers.data)

    def post(self,request,format=None):
        serializers = BookSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    

class BookDetails(APIView):
    def get(self,request,pk,format=None):
        books = Book.objects.all().get(pk=pk)
        serializers = BookSerializer(books,many=False)
        return Response(serializers.data)

  
class SearchResults(APIView):
    def get(self,request,book_title,format=None):
        books = Book.objects.all().filter(title=book_title)
        serializers = BookSerializer(books,many=True)
        return Response(serializers.data)  
    

class ReadingList(APIView):
    def get(self,request,user_id,format=None):
        books = Book.objects.all().filter(user_id=user_id)
        serializers = BookSerializer(books,many=True)
        return Response(serializers.data)
    

class MyBooks(APIView):
    def get(self,request,user_id,format=None):
        books = Book.objects.all().filter(user_id=user_id)
        serializers = BookSerializer(books,many=True)
        return Response(serializers.data)
    

class Comments(APIView):
    def get(self,request,pk,format=None):
        comments = Comment.objects.all().filter(book_id=pk)
        serializers = CommentSerializer(comments,many=True)
        return Response(serializers.data)

    def post(self,request,pk,format=None):
        serializers = CommentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    

class Ratings(APIView):
    def get(self,request,pk,format=None):
        ratings = Rating.objects.all().filter(book_id=pk)
        serializers = RatingSerializer(ratings,many=True)
        return Response(serializers.data)

    def post(self,request,pk,format=None):
        serializers = RatingSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)