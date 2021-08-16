from rest_framework.views import APIView
from rest_framework.response import Response


class PingPongView(APIView):
    def get(self, request):
        return Response({"msg": "pong"}, status=200)
