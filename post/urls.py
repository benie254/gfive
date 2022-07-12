from django.urls import path,re_path as url
from . import views
from post.views import RegisterView, LoginView, UserView, LogoutView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('api/users/register/', RegisterView.as_view()),
    path('api/users/login/', LoginView.as_view()),
    path('api/users/', views.AllRegisteredUsers.as_view()),
    path('api/user/', UserView.as_view()),
    path('api/users/logout', LogoutView.as_view()),
    path('api/books/',views.OurBookLibrary.as_view()),
    path('api/books/<int:pk>/',views.BookDetails.as_view()),
    path('api/books/search/title-<str:book_title>/',views.SearchResults.as_view()),
    path('api/books/comments/',views.AllComments.as_view()),
    path('api/books/<int:pk>/comments/',views.Comments.as_view()),
    path('api/books/ratings/',views.AllRatings.as_view()),
    path('api/books/<int:pk>/ratings/',views.Ratings.as_view()),
    path('api/user/<int:user_id>/bio/',views.UserBio.as_view()),
    path('api/user/<str:user_id>/books/',views.ReadingList.as_view()),
    path('api/user/<str:user_id>/books/',views.MyBooks.as_view()),
    url(r'^api-token-auth/', obtain_auth_token),
]