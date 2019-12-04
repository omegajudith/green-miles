from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """ creates and saves a user witha given email and password"""
        if not email:
            raise ValueError('User must have an email field')
        
        if not password:
            raise ValueError('User must provide a valid password')

        user = self.model(
            email=self.normalize_email(email), 
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
         """ creates and saves a superuser with emails and passwords"""
         user = self.create_user(email, password=password, **extra_fields)
         user.is_verified = True
         user.is_admin = True
         user.save(using=self._db)
         return user


class Role(models.Model):

    ADMIN = 1
    SUPPLIER = 2
    LOADER = 3
    RECIPIENT = 4
    ROLE_CHOICES = (
        (ADMIN, 'admin'),
        (LOADER, 'loader'),
        (SUPPLIER, 'suplier'),
        (RECIPIENT, 'recipient'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)
    def __str__(self):
        return self.get_id_display()




class User(AbstractBaseUser):
    GENDER = (('m', 'Male'),('f', 'Female'),('o', 'Other'))

    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(verbose_name='email adress', max_length=255, unique=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GENDER)
    location = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100)
    image = models.ImageField(max_length=30, blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    roles = models.ManyToManyField(Role)
    
    objects = UserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, sperm, obj=None):
        'Does the user have a specific permission?'
        return self.is_admin
    
    def has_module_perms(self, app_label):
        'Does the user have permissions to view the app_label'
        return True

    @property
    def is_staff(self):
        'Is the user a member of staff'
        return self.is_admin

    def get_long_name(self):
        return f"{self.first_name} {self.last_name}"
