from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView

from api.models import Profile, User
from api.serializers import ProfileSerializer
from domain.services.google import get_google_authenticator
from utils.jwt import encode


class PingPongView(APIView):
    def get(self, request):
        return Response({"msg": "pong"}, status=200)


class GetUserView(RetrieveAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()



class SignInUser(APIView):
    serializer = ProfileSerializer
    
    def get_queryset(self):
        return Profile.objects.all()

    def post(self, request):
        strategy = request.data.get('strategy', 'google')
        if strategy == 'google':
            token = request.data.get("token")
            user = get_google_authenticator().authenticate(google_jwt_token=token)
        userobj, created = User.objects.get_or_create(email=user.email, defaults= {"email":user.email})
        if created:
            status=201
            user = user.to_dict()
            user['user_id'] = userobj.uuid
            del user['email']
            profile = Profile.objects.create(**user)
        else:
            status=200
            profile = Profile.objects.get(user=userobj.uuid)
        serialize = self.serializer(profile)
        jwt = encode(serialize.data)
        return Response({"jwt": jwt}, status=status)

