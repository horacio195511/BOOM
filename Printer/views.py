from django.shortcuts import render
from django.http import HttpResponse
from BOOM.modelform import CreatePrinterForm
from Printer.serializer import PrinterModelSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from Printer.models import PrinterModel


def printercreate(request):
    if request.method == 'GET':
        form = CreatePrinterForm()
        context = {'title': 'Printer-Create',
                   'form': form,
                   'submitTitle': 'Create'}
        return render(request, 'form.html', context)
    elif request.method == 'POST':
        form = CreatePrinterForm(request.POST)
        form.save()
        return HttpResponse('Printer Created')


# API veiw
@csrf_exempt
def modellistupdate(request):
    # TODO: return an json file for the list
    if request.method == 'GET':
        # get the company name
        company = request.GET['company']
        modelList = PrinterModel.objects.filter(printer_company=company)
        # transform the list in to json
        serializer = PrinterModelSerializer(modelList, many=True)
        return JsonResponse(serializer.data, safe=False)
