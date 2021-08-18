from abc import ABC, abstractmethod
from domain.models import Profile


class OAuthStrategy(ABC):
    @abstractmethod
    def get_user_for_credentials(self, *args, **kwargs) -> Profile:
        raise NotImplementedError()
