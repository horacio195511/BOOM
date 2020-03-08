from django.db import models
from BOOM.db_param import MaxLength

# Create your models here.


class Thing(models.Model):
    name = models.CharField(max_length=MaxLength.name)
    file = models.FileField(upload_to='thing')