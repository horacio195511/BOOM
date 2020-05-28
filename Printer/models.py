from django.db import models
from BOOM.db_param import MaxLength


# Create your models here.


class PrinterCompany(models.Model):
    name = models.CharField(max_length=MaxLength.name)


class PrinterModel(models.Model):
    printer_company = models.ForeignKey(PrinterCompany, on_delete=models.CASCADE)
    name = models.CharField(max_length=MaxLength.name)


class Printer(models.Model):
    name = models.CharField(max_length=MaxLength.name)
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    model_company = models.ForeignKey(PrinterCompany, on_delete=models.CASCADE)
    model_model = models.ForeignKey(PrinterModel, on_delete=models.CASCADE)
    # speed is calculated in mm/s
    speed = models.IntegerField()
    # TODO: printing quality is first set by maker and then score by user.
    quality = models.IntegerField()
    address = models.CharField(max_length=MaxLength.address)
