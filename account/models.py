from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, name, username, email, password=None):
        """
        Creates and saves a user with the given name, username, email and password.
        """
        if not username:
            raise ValueError('User must have a username')

        if not email:
            raise ValueError('User must have a valid email')

        user = self.model(
            name=name,
            username=username,
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, username, email, password=None):
        """
        Creates and saves a superuser with the given name, username, email and password.
        """
        user = self.create_user(
            name=name,
            username=username,
            email=self.normalize_email(email),
            password=password,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.superadmin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=50)
    # Required Field
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, add_label):
        return True
