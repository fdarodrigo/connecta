# Developer's imports
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Models' imports
from .models import CustomUser


# Form to create new users
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            "email",
            'first_name',
            'last_name',
            'user_image',
            )


# A form to update new users
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "is_active",
            'first_name',
            'last_name',
            )
