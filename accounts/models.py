from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
import uuid
# Create your models here.

class UserManager(BaseUserManager):


    def create_user(self,email,password,**extra_fields):

        if not email:

            return ValueError("Email must be there")
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(self.db)

        return user
    
    def create_superuser(self,email,password,**extra_fields):

        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:

            raise ValueError(("Super user must have is_staff True. "))

        return self.create_user(email,password,**extra_fields)



class User(AbstractUser):

    username = models.CharField(max_length=30,unique=True,null=True)
    email = models.CharField(max_length=60,primary_key=True)
    phone = models.CharField(max_length=20,null=True)
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):

        return self.email
    
    