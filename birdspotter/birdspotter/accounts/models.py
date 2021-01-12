from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.db import models


class User(AbstractUser):
    """Custom user implementation

    Attributes:
        username (str): user specified username, used as unique identifier
    """

    username = models.CharField(max_length=30, unique=True)

    def save(self, *args, **kwargs):
	    self.password = make_password(self.password)
	    super(User, self).save(*args, **kwargs)
