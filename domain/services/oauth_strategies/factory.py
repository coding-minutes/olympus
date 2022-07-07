from domain.services.oauth_strategies.implementations.google import GoogleOAuthStrategy
from domain.services.oauth_strategies.implementations.github import GithubOAuthStrategy


class OAuthFactory:
    _DEFAULT_SERVICE = GoogleOAuthStrategy
    _SERVICE_MAP = {
        "google": GoogleOAuthStrategy,
        "github": GithubOAuthStrategy,
    }

    @classmethod
    def get(cls, name=None):
        strategy = cls._SERVICE_MAP.get(name, cls._DEFAULT_SERVICE)

        return strategy()
