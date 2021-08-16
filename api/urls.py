from django.urls import path, include
from api.views import PingPongView

urlpatterns = [path("ping/", PingPongView.as_view())]
