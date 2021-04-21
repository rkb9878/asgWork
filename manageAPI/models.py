from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.


class userManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User Must have an Email.")
        if not username:
            raise ValueError("User Must have an username.")

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """
    Creating Custome User Model
    """
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True, db_index=True)
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True)
    bio = models.TextField(null=True)
    profilePic = models.ImageField(upload_to='profile/')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    joined_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    objects = userManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Business(models.Model):
    """
    asuming registrationNo will be the auto increment and unique for each and every business
    """
    registrationNo = models.IntegerField(unique=True)
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    name = models.CharField(max_length=255, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return self.email


class Products(models.Model):
    """user
    product model
    """
    name = models.CharField(max_length=255, db_index=True)
    mrp = models.FloatField()
    description = models.TextField()
    image1 = models.ImageField(upload_to='product/')
    image2 = models.ImageField(upload_to='product/')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CharField, null=True, blank=True)

    def __str__(self):
        return self.name
