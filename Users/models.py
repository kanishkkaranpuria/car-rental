from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from django.contrib.auth import get_user_model

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, name=None, is_active=True, password=None, is_staff=False, is_admin=False, ):
        if not email:
            raise ValueError("Users must have an email address")
        # if not password:
        #     raise ValueError("Users must have a password")
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password) 
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.name = name
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None, name=None):
        user = self.create_user(
                email,
                name,
                password=password,
                is_staff=True
        )
        return user

    def create_superuser(self, email, password=None, name=None):
        user = self.create_user(
                email,
                name,
                password=password,
                is_staff=True,
                is_admin=True
        )
        return user

class User(AbstractBaseUser):
    name     = models.CharField(max_length=250,blank=True,null=True,default='')
    email    = models.EmailField(max_length=255,unique=True)
    staff    = models.BooleanField(default=False)
    admin    = models.BooleanField(default=False)
    active   = models.BooleanField(default=False) 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email  

    def get_short_name(self):
        return self.name  

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @is_staff.setter
    def is_staff(self, value):
        self.staff = value    

    @property
    def is_admin(self):
        return self.admin 

    @is_admin.setter
    def is_admin(self, value):
        self.admin = value
            
    @property
    def is_active(self):
        return self.active

    @is_active.setter
    def is_active(self, value):
        self.active = value

    @property
    def is_superuser(self):
        return self.staff and self.admin and self.active

User = get_user_model()
