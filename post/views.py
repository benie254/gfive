from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from post.serializer import BookSerializer,RatingSerializer,CommentSerializer
from post.models import Book,Rating,Comment,Profile   
from rest_framework import status
from .serializer import UserSerializer,ProfileSerializer
from .models import User
import jwt, datetime
from rest_framework.generics import CreateAPIView
from rest_framework import permissions


# Create your views here.
# class RegisterView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
class RegisterView(CreateAPIView):
    model = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response
    
class AllRegisteredUsers(APIView):

    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data)


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
    

class AllUserProfiles(APIView):
    def get(self,request,user_id,format=None):
        profiles = Profile.objects.all()
        serializers = ProfileSerializer(profiles,many=True)
        return Response(serializers.data)
    

class UserProfile(APIView):
    def get(self,request,user_id,format=None):
        profile = Profile.objects.all().get(pk=user_id)
        serializers = ProfileSerializer(profile,many=False)
        return Response(serializers.data)
   
    def post(self,request,user_id,format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


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
    def get(self,request,book_id,format=None):
        books = Book.objects.all().get(pk=book_id)
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
    

class AllComments(APIView):
    def get(self,request,format=None):
        comments = Comment.objects.all()
        serializers = CommentSerializer(comments,many=True)
        return Response(serializers.data)  
    

class BookComments(APIView):
    def get(self,request,book_id,format=None):
        comments = Comment.objects.all().filter(pk=book_id)
        serializers = CommentSerializer(comments,many=True)
        return Response(serializers.data)

    def post(self,request,book_id,format=None):
        serializers = CommentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class AllRatings(APIView):
    def get(self,request,format=None):
        ratings = Rating.objects.all()
        serializers = RatingSerializer(ratings,many=True)
        return Response(serializers.data)
    

class BookRatings(APIView):
    def get(self,request,book_id,format=None):
        ratings = Rating.objects.all().filter(pk=book_id)
        serializers = RatingSerializer(ratings,many=True)
        return Response(serializers.data)

    def post(self,request,book_id,format=None):
        serializers = RatingSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)