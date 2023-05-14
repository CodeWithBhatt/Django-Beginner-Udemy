from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """Default Manager for UserProfile
    """
    def create_user(self, email:str, name:str, password=None):
        """Create a new user profile

        Args:
            email (str): email for verification of user
            name (str): name of user
            password (_type_, optional): password with minimum length of 6. Defaults to None.

        Returns:
            user: user object of new created user
        """
        if not email:
            raise ValueError("Email must have an email address")
        Email = self.normalize_email(email)
        User = self.model(email=Email, name=name)
        User.set_password(password)
        User.save(using=self._db)

        return User

    def create_superUser(self, email, name, password):
        """Create a new super user"""
        User = self.create_user(email, name, password)
        User.is_superuser = True
        User.is_staff = True
        User.save(using=self._db)

        return User


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database Model for User Profiles

    Args:
        AbstractBaseUser : Null
        PermissionsMixin : Null
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrive full name"""
        return self.name

    def get_short_name(self):
        """Retrive first name"""
        return self.name.split(' ')[0]

    def __str__(self):
        """Represent string representation of user"""
        return self.email
