from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .managers import (
    CustomUserManager,
    AdminUserManager,
    EmployeeUserManager,
    ClientUserManager,
)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class AdminUser(CustomUser):
    objects = AdminUserManager()


class EmployeeUser(CustomUser):
    objects = EmployeeUserManager()


class ClientUser(CustomUser):
    objects = ClientUserManager()
