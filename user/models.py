from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import uuid

AUTH_PROVIDERS = (
    ("email", "Email"),
    ("google", "Google"),
)
class MyUserManager(BaseUserManager): 

    def create_user(self, email,first_name=None, last_name=None,  password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),first_name=first_name, last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,  password=None ):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
         
        )
        user.is_admin = True
    
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,  unique=True, editable=False)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    auth_provider = models.CharField(max_length=50, choices=AUTH_PROVIDERS, default="email")

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =[]


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin