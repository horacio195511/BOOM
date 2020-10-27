from CMS.models import NEWS
from Market.models import Thing, Order
from Printer.models import Printer, PrinterModel, PrinterCompany
from User.models import User, Customer
from django.forms import ModelForm, Textarea
from django import forms


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class CreateNewsForm(ModelForm):
    class Meta:
        model = NEWS
        fields = ['title', 'article', 'image']


class CreateThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'file', 'image', 'description', 'owner', 'price']
        widgets = {
            'description': Textarea(attrs={'col': 50, 'row': 50})
        }


class CreatePrinterForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreatePrinterForm, self).__init__(*args, **kwargs)
        self.fields['model_company'].queryset = PrinterCompany.objects.values_list('name')
        self.fields['model_company'].widget.attrs.update({'onchange': 'reloadList()', 'id': 'model_company'})
        # TODO: delete the default list in production
        preModelList = PrinterModel.objects.filter(printer_company=8).values_list('name')
        self.fields['model_model'].queryset = preModelList
        self.fields['model_model'].widget.attrs.update({'id': 'model_model'})

    class Meta:
        # TODO: dynamically load the model list of a specific company
        model = Printer
        fields = ['name', 'width', 'height', 'model_company', 'model_model', 'speed', 'quality', 'address']


class CreateOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['thing', 'amount', 'sentTo']
