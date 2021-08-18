from django.urls import path, include
from api.views import GetUserView, SignInUser, VerifyView

urlpatterns = [
    path("users/<pk>", GetUserView.as_view()),
    path("users/signin/", SignInUser.as_view()),
    path("sessions/verify/", VerifyView.as_view()),
]
