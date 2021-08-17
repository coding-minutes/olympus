from django.urls import path, include
from api.views import PingPongView, GetUserView, SignInUser

urlpatterns = [
    path("ping/", PingPongView.as_view()),
    path("users/<pk>", GetUserView.as_view()),
    path('users/signin/', SignInUser.as_view()),
]
