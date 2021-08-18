from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from api.models import Profile, User
from utils.jwt import encode, decode
from domain.services.oauth_strategies.factory import OAuthFactory
from jwt.exceptions import DecodeError
from domain.errors import InvalidCredentials


class GetUserView(GenericAPIView):
    queryset = Profile.objects.all()

    def get(self, request, *args, **kwargs):
        profile = self.get_object()
        return Response({"data": profile.to_domain_model().to_dict()})


class SignInUser(APIView):
    queryset = Profile.objects.all()

    def post(self, request):
        strategy = request.data.get("strategy", "google")
        try:
            profile = OAuthFactory.get(name=strategy).get_user_for_credentials(
                **request.data.get("data")
            )
        except InvalidCredentials:
            return Response({"error": "Invalid Credentials"},status=401)
        jwt = encode(profile.to_dict())
        return Response({"jwt": jwt})


class VerifyView(APIView):
    def post(self, request, *args, **kwargs):
        jwt = request.data.get("jwt")

        try:
            data = decode(jwt)
            uuid = data["id"]
            User.objects.get(pk=uuid)
            return Response({"verified": True}, status=200)
        except (DecodeError, User.DoesNotExist):
            return Response({"verified": False}, status=401)
