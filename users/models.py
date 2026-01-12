from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser,Group,Permission
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set', 
        blank=True,
        help_text='Specific permissions for this user.'
    )
    bio = models.TextField(blank=True, null=True) 
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    def __str__(self):
        return self.username


class Skill(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='skills/')

    def __str__(self):
        return f"{self.teacher.username} - {self.name}"