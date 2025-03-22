from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# ✅ Custom Admin User Model
class AdminUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = None  # Remove default username field

    groups = models.ManyToManyField(Group, related_name="admin_users")
    user_permissions = models.ManyToManyField(Permission, related_name="admin_users_permissions")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

# ✅ Book Model
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    available_copies = models.IntegerField(default=1)

    def __str__(self):
        return self.title

