from CMS.models import NEWS
from Market.models import Thing, Order
from Printer.models import Printer
from User.models import User, Customer
from django.forms import ModelForm


# TODO: migrate to ModelForm implementation
class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']


class CreateNewsForm(ModelForm):
    class Meta:
        model = NEWS
        fields = ['title', 'article', 'image']


class CreateThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'file', 'image', 'description', 'owner', 'price']


class CreatePrinterForm(ModelForm):
    class Meta:
        model = Printer
        fields = ['name', 'width', 'height', 'model_company', 'model_model', 'speed', 'quality', 'address']


class CreateOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['thing', 'amount']
