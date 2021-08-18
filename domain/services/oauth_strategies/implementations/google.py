import requests
from domain.services.oauth_strategies.interface import OAuthStrategy
from api.models import User, Profile
from domain.errors import InvalidCredentials


class GoogleOAuthStrategy(OAuthStrategy):
    def get_user_for_credentials(self, token):
        response = requests.get(
            f"https://oauth2.googleapis.com/tokeninfo?id_token={token}"
        )

        data = response.json()
        if 'error' in data:
            raise InvalidCredentials()
            
        user, created = User.objects.get_or_create(
            email=data["email"], defaults={"email": data["email"]}
        )
        profile, created = Profile.objects.get_or_create(
            user=user,
            defaults={
                "first_name": data["given_name"],
                "last_name": data["family_name"],
                "user": user,
                "photo": data["picture"],
            },
        )
        return profile.to_domain_model()
