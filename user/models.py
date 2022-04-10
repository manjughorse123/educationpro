from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from enum import Enum
from django.template.defaultfilters import slugify

# Create your models here.

class TimeStampeModel(models.Model):

   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
         abstract = True

class UserRoleEnum(Enum):
    Teacher = 1
    Student = 2




class GenderEnum(Enum):
    Male = 1
    Female = 2


class UserManager(BaseUserManager):
   
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)



class User(AbstractBaseUser,TimeStampeModel):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    user_role = models.CharField(
      max_length=19,
      choices=[(tag.value, tag) for tag in UserRoleEnum]  # Choices is a list of Tuple
    )
    gender  = models.CharField(
      max_length=10,
      choices=[(tag.value,tag) for tag in GenderEnum]  # Choices is a list of Tuple
    )
    location = models.CharField(max_length=255)
    email = models.CharField(max_length=20 , unique= True)
    slug = models.SlugField(max_length=255)

    password = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    mobile = models.CharField(max_length=55)
    otp = models.CharField(max_length=20)
    otp_is_verified = models.BooleanField(default=False)
    otp_is_expired = models.DateTimeField(null=True)
    image = models.URLField(null=True, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['first_name','phone']


    objects = UserManager()

    def __str__(self):
        return self.email
    