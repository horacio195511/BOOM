from django.shortcuts import render
from django.http import HttpResponse
from BOOM.modelform import CreatePrinterForm


# Create your views here.

def createPrinter(request):
    if request.method == 'GET':
        form = CreatePrinterForm()
        context = {'title': 'Printer-Create',
                   'action': 'createPrinter',
                   'form': form,
                   'submitTitle': 'Create'}
        return render(request, 'Printer/createPrinter.html', context)
    elif request.method == 'POST':
        form = CreatePrinterForm(request.POST)
        form.save()
        return HttpResponse('Printer Created')
