from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """Helps django work with our custom user model"""

    def create_user(self, email, name, password=None):
        """create a new user profile object"""

        if not email:
            raise ValueError('user must have an email address')
        email = self.normalize_email(email)       # convert all to lowercase
        user = self.model(email=email)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,name,password):
        """creates and saves a new superuser with given details."""
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """
    Represents a 'user profile' inside our system
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """used to get a users full name"""
        return self.name

    def get_short_name(self):
        """used to get a users short name"""
        return self.name

    def __str__(self):
        """django uses this when it needs to convert a object to a string"""
        return self.email



class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status_text















