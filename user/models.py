from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,email,password=None,**extrafields):
        if not email:
            raise ValueError("Email is a required field")
        user = self.model(email=self.normalize_email(email),**extrafields)
        user.set_password(password)
        user.save(using= self._db)
        return user

    def create_superuser(self,email,password,**extrafields):
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(max_length=255,unique=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()
    REQUIRED_FIELDS = ['password']
    def __str__(self):
        return self.email