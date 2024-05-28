#profiles/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


#___________________________________________________________ProfileManager
class ProfileManager(BaseUserManager):
    
      def create_user(self, email, username, first_name, last_name, password=None, **extra_fields):
            if not email:
                  raise ValueError('Email is required')
            if not username:
                  raise ValueError("Users must have a user name")
            
            user = self.model(
                  email=self.normalize_email(email),
                  username=username,
                  first_name=first_name,
                  last_name=last_name,
                  **extra_fields
            )
            user.set_password(password)
            user.save(using=self._db)
            return user

      def create_superuser(self, email, username, first_name, last_name, password=None):
            user = self.create_user(
                  email=email,
                  username=username,
                  first_name=first_name,
                  last_name=last_name,
                  password=password,
            )
            user.is_admin = True
            user.is_staff = True
            user.is_active = True
            user.save(using=self._db)
            return user

#___________________________________________________________Profile
class Profile(AbstractBaseUser):
      username          = models.CharField(max_length=50, unique=True)
      first_name        = models.CharField(max_length=50)
      last_name         = models.CharField(max_length=50)
      email             = models.EmailField(max_length=100, unique=True)
      phone_number      = models.CharField(max_length=50)
      profile_picture = models.ImageField(blank=True, null=True, upload_to='profile/')
      date_joined       = models.DateTimeField(auto_now_add=True)
      last_login        = models.DateTimeField(auto_now_add=True)
      is_admin          = models.BooleanField(default=False)
      is_staff          = models.BooleanField(default=False)
      is_active         = models.BooleanField(default=False)
      is_inactive       = models.BooleanField(default=False)
      is_published      = models.BooleanField(default=False)

      # Login with email
      USERNAME_FIELD = 'email'
      REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

      objects = ProfileManager()

      def __str__(self):
            return self.email

      def has_perm(self, perm, obj=None):
            return self.is_admin

      def has_module_perms(self, app_label):
            return True


