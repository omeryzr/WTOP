from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Member(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    points = models.PositiveIntegerField(default=0)
    points_counter = models.PositiveIntegerField(default=0)#how many peoples give vote
    active = models.BooleanField(default=True, editable=False)
    cdate = models.DateTimeField(auto_now_add=True)