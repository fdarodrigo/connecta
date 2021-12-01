#  Django's imports
from django.db import models

# Developer's imports
from django.contrib.auth.models import AbstractUser

# Managers' imports
from .managers import CustomUserManager


# Custom user model
class CustomUser(AbstractUser):
    username = None
    # The default user already have an email, but for default this email not is unique
    # email must be unique for any users, for acess
    email = models.EmailField("Email", unique=True)
    first_name = models.CharField("First Name", max_length=100)
    last_name = models.CharField('Last Name', max_length=100)
    user_image = models.ImageField("User Image", upload_to="images/", blank=True)
    is_active = models.BooleanField(default=False)

    # Here we can select parameters for login and forms
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    # All objects will be manager by UserManager class
    objects = CustomUserManager()

    def __str__(self):
        return self.email
