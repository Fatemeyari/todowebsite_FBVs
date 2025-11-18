from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """ Manager for custom User model to handle user creation and superuser creation. """

    def create_user(self, username , password , **kwargs):
        """
        Create and save a regular User with the given username and password.
        """
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)

        if not username:
            raise ValueError(_("The username must be set"))
        if kwargs.get('email'):
            email=self.normalize_email(kwargs.get('email'))
        user=self.model(username=username,**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **kwargs):
        """
        Create and save a Superuser with the given username and password.
        """
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if kwargs.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(username, password, **kwargs)


class User(AbstractBaseUser,PermissionsMixin):
    """ Custom User model."""
    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.username


    class Meta :
        ordering = ['-created_time']
        verbose_name_plural = 'Users'
        verbose_name='User'