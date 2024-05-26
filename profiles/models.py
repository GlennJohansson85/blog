from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


#___________________________________________________________ProfileManager
class ProfileManager(BaseUserManager):
    
      def create_user(self, user_name, first_name, last_name, email, password=None, **extra_fields):
            if not email:
                  raise ValueError('Email is required')
            
            email = self.normalize_email(email)
            user = self.model(
                  user_name=user_name,
                  email=email,
                  first_name=first_name,
                  last_name=last_name,
                  **extra_fields
            )
            user.set_password(password)
            user.save(using=self._db)
            return user

      def create_superuser(self, user_name, first_name, last_name, email, password=None, **extra_fields):
            extra_fields.setdefault('is_admin', True)
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_active', True)

            if extra_fields.get('is_admin') is not True:
                  raise ValueError('Superuser must have is_admin=True.')
            if extra_fields.get('is_staff') is not True:
                  raise ValueError('Superuser must have is_staff=True.')

            return self.create_user(user_name, first_name, last_name, email, password, **extra_fields)

#___________________________________________________________Profile
class Profile(AbstractBaseUser):
      user_name = models.CharField(max_length=50, unique=True)
      first_name = models.CharField(max_length=50)
      last_name = models.CharField(max_length=50)
      email = models.EmailField(max_length=100, unique=True)
      phone_number = models.CharField(max_length=50)
      profile_picture = models.ImageField(blank=True, upload_to='profile/')
      date_joined = models.DateTimeField(auto_now_add=True)
      last_login = models.DateTimeField(auto_now_add=True)
      is_admin = models.BooleanField(default=False)
      is_staff = models.BooleanField(default=False)
      is_active = models.BooleanField(default=False)
      is_inactive = models.BooleanField(default=False)
      is_published = models.BooleanField(default=False)

      # Login with email
      USERNAME_FIELD = 'email'
      REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name']

      objects = ProfileManager()

      def full_name(self):
            return f'{self.first_name} {self.last_name}'

      def __str__(self):
            return self.email

      def has_perm(self, perm, obj=None):
            return self.is_admin

      def has_module_perms(self, add_label):
            return True


