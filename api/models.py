from django.db import models
import uuid
from domain.models import Profile as DomainProfile


class User(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    photo = models.URLField()

    def to_domain_model(self):
        return DomainProfile(
            first_name=self.first_name,
            last_name=self.last_name,
            photo=self.photo,
            email=self.user.email,
            id=str(self.user.uuid),
        )
