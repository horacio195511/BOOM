from django.shortcuts import render
from django.http import HttpResponse
from BOOM.modelform import CreatePrinterForm


# Create your views here.

def printercreate(request):
    if request.method == 'GET':
        # TODO: how to get the company name in the form: JavaScript AJAX!!
        form = CreatePrinterForm('0')
        context = {'title': 'Printer-Create',
                   'form': form,
                   'submitTitle': 'Create'}
        return render(request, 'form.html', context)
    elif request.method == 'POST':
        form = CreatePrinterForm(request.POST)
        form.save()
        return HttpResponse('Printer Created')
