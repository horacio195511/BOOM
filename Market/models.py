from django.db import models
from BOOM.db_param import MaxLength
from django.contrib.auth.models import User
from Printer.models import Printer
from User.models import Customer


class Thing(models.Model):
    name = models.CharField(max_length=MaxLength.name)
    file = models.FileField(upload_to='thing')
    image = models.ImageField(upload_to='image/things', max_length=MaxLength.image, default='image')
    description = models.CharField(max_length=MaxLength.description, default='description')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()


class Order(models.Model):
    # cartID is used to group the order in the same cart, which also make thing replicate more flexible
    # set to 0 after
    printer = models.ForeignKey(Printer, on_delete=models.CASCADE)
    thing = models.ForeignKey(Thing, on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.IntegerField()
    # state is a number between 1~22
    state = models.CharField(max_length=MaxLength.state)
    sentTo = models.CharField(max_length=MaxLength.address)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # TODO: get the geolocation from google api
