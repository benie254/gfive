from django.urls import path,re_path as url
from . import views


urlpatterns = [
    path('api/books/',views.OurBookLibrary.as_view()),
]