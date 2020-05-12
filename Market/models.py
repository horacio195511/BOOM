from django.db import models
from BOOM.db_param import MaxLength
from django.contrib.auth.models import User


# Create your models here.


class Thing(models.Model):
    name = models.CharField(max_length=MaxLength.name)
    file = models.FileField(upload_to='thing')
    image = models.ImageField(upload_to='image/things', max_length=MaxLength.image, default='image')
    description = models.CharField(max_length=MaxLength.description, default='description')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
