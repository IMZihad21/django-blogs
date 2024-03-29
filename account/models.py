from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from account.manager import CustomUserManager


class User(AbstractUser):
    """
    Disable default username and use email as username
    """

    username = None

    avatar = models.ImageField(upload_to="users/avatars/%Y/%m/%d/", blank=True)
    email = models.EmailField(
        _("Email Address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ["-date_joined"]
