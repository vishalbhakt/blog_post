from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

   
    def __str__(self):
        return self.title
    

class CustomUser(AbstractUser):
    # ROLE_CHOICES = [
    #     ('author', 'Author'),
    #     ('admin', 'Admin'),
    # ]
    # role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='author')

    groups = models.ManyToManyField(Group, related_name="customuser_groups") 
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions")