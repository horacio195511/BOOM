from django.db import models
from BOOM.db_param import MaxLength


# Create your models here.


class NEWS(models.Model):
    title = models.CharField(max_length=MaxLength.title)
    article = models.CharField(max_length=MaxLength.article)
    image = models.ImageField(upload_to='image/news', max_length=MaxLength.image, default='image')
