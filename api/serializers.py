from rest_framework import serializers
from api.models import Profile, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = Profile
        fields = ["user", "first_name", "last_name", "photo"]
