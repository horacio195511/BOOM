from django.db import models
from BOOM.db_param import MaxLength
from django.contrib.auth.models import User
from User.models import Customer


# Create your models here.


class Thing(models.Model):
    name = models.CharField(max_length=MaxLength.name)
    file = models.FileField(upload_to='thing')
    image = models.ImageField(upload_to='image/things', max_length=MaxLength.image, default='image')
    description = models.CharField(max_length=MaxLength.description, default='description')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # TODO: makemigration for the price field
    price = models.IntegerField()


class Order(models.Model):
    # TODO: makemigration to the database
    # TODO: an order that could be a set of order, like a shopping cart
    # cartID is used to group the order in the same cart, which also make thing replicate more flexible
    # TODO: cartID should be generated from userID and datetime
    cartID = models.IntegerField()
    created_datetime = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    maker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='maker')
    thing = models.ForeignKey(Thing, on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.IntegerField()
    state = models.CharField(max_length=MaxLength.state)
