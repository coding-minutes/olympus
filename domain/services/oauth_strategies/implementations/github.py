import requests
from domain.services.oauth_strategies.interface import OAuthStrategy
from api.models import User, Profile
from domain.errors import InvalidCredentials
from olympus.config import Config


class GithubOAuthStrategy(OAuthStrategy):
    def get_user_for_credentials(self, code) -> Profile:
        payload = {
            "client_id": Config.GITHUB_CLIENT_ID,
            "client_secret": Config.GITHUB_CLIENT_SECRET,
            "code": code,
        }
        headers = {"Accept": "application/json"}

        # Get the OAuth Token
        response = requests.post(
            "https://github.com/login/oauth/access_token", json=payload, headers=headers
        )
        data = response.json()

        if "error" in data:
            raise InvalidCredentials()

        access_token = data["access_token"]

        headers = {"Authorization": f"token {access_token}"}

        # Get the email
        response = requests.get("https://api.github.com/user/emails", headers=headers)
        data = response.json()

        email = data[0]["email"]

        # Get the user info
        response = requests.get("https://api.github.com/user", headers=headers)
        data = response.json()

        name = data["name"]
        firstName, lastName = name.split(" ")

        user, created = User.objects.get_or_create(
            email=email, defaults={"email": email}
        )
        profile, created = Profile.objects.get_or_create(
            user=user,
            defaults={
                "first_name": firstName,
                "last_name": lastName,
                "user": user,
                "photo": data["avatar_url"],
            },
        )
        return profile.to_domain_model()
