# Developer's imports
from django.contrib.auth.models import BaseUserManager


# This is a user management, it will be response to save all users (normal and admin user's)
class CustomUserManager(BaseUserManager):
    """
    The function will manage other functions (create_user and create_superuser). Because user
    have to log in with password and email

    **extra_fileds are optionals
    """

    def create_user(self, email, password, **extra_fields):
        # Force email is required
        if not email:
            raise ValueError("Email is required!")
        # Normalize email minimazing user's erros
        email = self.normalize_email(email)
        # Use's model, forcing email use
        user = self.model(email=email, **extra_fields)
        # set_password for criptographing password
        user.set_password(password)
        # Change the default value is_active, users must be accepted by institution
        user.is_active = True
        # Saving user in database
        user.save()
        return user

    """
    This function will create a new super user

    With all privileges corresponding a superuser equal True
    """

    def create_superuser(self, email, password, **extra_fields):
        # Defining values to extra_fields
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        # Condicionals for confirm superuser
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must to be is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must to be is_superuser=True")

        # _create_user will be receive the data, normalize email, verify is user already exist and create a new super user
        return self.create_user(email, password, **extra_fields)
