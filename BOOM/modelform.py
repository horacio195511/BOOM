from CMS.models import NEWS
from Market.models import Thing, Order
from Printer.models import Printer
from User.models import User, Customer
from django.forms import ModelForm


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = []


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = []


class CreateNewsForm(ModelForm):
    class Meta:
        model = NEWS
        fields = []


class CreateThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = []


class CreatePrinterForm(ModelForm):
    class Meta:
        model = Printer
        fields = []


class CreateOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = []
