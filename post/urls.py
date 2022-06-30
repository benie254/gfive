from django.urls import path,re_path as url
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('api/books/',views.OurBookLibrary.as_view()),
    path('api/<int:pk>/comments/',views.Comments.as_view()),
    url(r'^api-token-auth/', obtain_auth_token),
]