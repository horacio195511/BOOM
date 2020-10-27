from rest_framework import serializers
from Printer.models import PrinterModel


class PrinterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrinterModel
        fields = ['name']
