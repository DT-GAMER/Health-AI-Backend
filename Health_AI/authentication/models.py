from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()  # Get the user model

# Custom manager for the CustomUser model
class CustomUserManager(BaseUserManager):
    """
    Custom manager for the CustomUser model.
    """

    # Creates a user with email, username, and password
    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email, username, and password.
        """
        # Validate email and username
        if not email:
            raise ValueError("Users must have an email address.")
        if not username:
            raise ValueError("Users must have a username.")

        # Create and save the user
        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Creates a superuser with email, username, and password
    def create_superuser(self, email, username, password):
        """
        Creates and saves a superuser with the given email, username, and password.
        """
        user = self.create_user(email=email, username=username, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Custom User model for authentication
class CustomUser(AbstractBaseUser):
    """
    Custom User model for authentication.
    """

    # Fields for email, username, and user status
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    username = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()  # Manager for CustomUser model

    USERNAME_FIELD = "email"  # Field used for authentication (email)
    REQUIRED_FIELDS = ["username"]  # Required fields when creating a user

    # String representation of the User model
    def __str__(self):
        return self.email



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
