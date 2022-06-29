from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from postApp.serializer import BookSerializer
from postApp.models import Book 

# Create your views here.
class OurBookLibrary(APIView):
	# permission_classes = (IsAdminOrReadOnly,IsAuthenticatedOrReadOnly)
	def get(self,request,format=None):
		books = Book.objects.all()
		serializers = BookSerializer(books,many=True)
		return Response(serializers.data)