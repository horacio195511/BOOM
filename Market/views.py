from django.shortcuts import render, redirect
from django.http import JsonResponse
from BOOM.modelform import CreateThingForm, CreateOrderForm
from Market.models import Thing, Order
from Market.serializers import ThingSerializer
from django.views.decorators.csrf import csrf_exempt


def thingcreate(request):
    if request.method == 'GET':
        form = CreateThingForm(initial={'owner': request.user})
        context = {'title': 'Thing-Create',
                   'form': form,
                   'submitTitle': 'Create'}
        return render(request, 'Form.html', context)
    elif request.method == 'POST':
        form = CreateThingForm(request.POST, request.FILES)
        form.save()
        return render(request, 'Action/success.html', {'action': 'create thing'})


def market(request):
    if request.method == "GET":
        things = []
        for thing in Thing.objects.all():
            things.append(thing)
        # TODO: there should be a way to identify the thing user choose in market.
        #   directly use pk of thing is the simplest solution.
        return render(request, 'Market/market.html', {'thing_list': things[-7:]})


def ordercreate(request, thingpk):
    if request.method == 'GET':
        form = CreateOrderForm(initial={'owner': request.user})
        context = {'title': 'Order-Create',
                   'form': form,
                   'submitTitle': 'Create'}
        return render(request, 'Form.html', context)
    elif request.method == 'POST':
        form = CreateOrderForm(request.POST)
        form.save()
        # TODO: the output should depends on OMS
        return render(request, 'Action/success.html', {'action': 'create order'})


@csrf_exempt
def apithinglist(request):
    if request.method == 'GET':
        things = Thing.objects.all()
        serializer = ThingSerializer(things, many=True)
        return JsonResponse(serializer.data, safe=False)

# def confirmOrder(request):
#     if request.method == 'GET':
#         return render(request, 'Market/confirmOrder.html')
#     elif request.method == 'POST':
