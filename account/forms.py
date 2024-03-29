from django.contrib.auth.forms import UserCreationForm

from account.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "avatar",
            "email",
            "password1",
            "password2",
        )
