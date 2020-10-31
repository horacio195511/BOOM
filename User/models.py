from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    # User field reference
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="image/user")
