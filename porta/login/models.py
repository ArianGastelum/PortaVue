from django.db import models

# Create your models here.
class Login(models.Model):
    email = models.TextField
    password = models.TextField()