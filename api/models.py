from django.db import models
import uuid


class User(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    photo = models.ImageField(null=True, blank=True)
