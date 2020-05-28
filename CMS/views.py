from django.shortcuts import render
from django.http import HttpResponse
from BOOM.modelform import CreateNewsForm
from CMS.models import NEWS


# Create your views here.

def createNews(request):
    if request.method == 'GET':
        form = CreateNewsForm()
        context = {'title': 'NEWS-Create',
                   'action': 'createnews',
                   'form': form,
                   'submitTitle': 'Create'}
        return render(request, 'Form.html', context)
    elif request.method == 'POST':
        form = CreateNewsForm(request.POST)
        form.save()
        return HttpResponse('NEWS Created')


def cms(request):
    # TODO: control center for the whole website, got the highest authority to all file
    #   customer account, thing, order and other shit.
    # TODO: build the authorization system
    return render(request, 'CMS/control_center.html')
