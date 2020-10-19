from django.shortcuts import render, redirect
from django.http import JsonResponse
from BOOM.modelform import CreateThingForm, CreateOrderForm
from Market.models import Thing, Order, Cart
from Market.serializers import ThingSerializer
from OMS.dispatcher import Dispatcher
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
    '''
    :param request:
    :param thingpk: thing user pick from webpage
    :return: the form with thing's information in it
    ordercreate only show the order and thing list auto pair algorithm make
    and user do the final check
    '''
    if request.method == 'GET':
        thing = Thing.objects.get(id=thingpk)
        form = CreateOrderForm(initial={'thing': thingpk})
        context = {'title': 'Order-Create',
                   'form': form,
                   'submitTitle': 'Create'}
        request.session["thingID"] = thingpk
        return render(request, 'Form.html', context)
    elif request.method == 'POST':
        thing = request.session["thingID"]
        price = thing.price * request.POST["amount"]
        order = Order(thing=thing, amount=request.POST["amount"], price=price, state=0)
        order.save()
        return render(request, 'Action/success.html', {'action': 'create order'})


def cartSent(request):
    # sent the order to the maker in the orderlist
    # get the cart of user
    if request.method == "POST":
        user = request.user
        orderList = Dispatcher.find_printer(user)
        # TODO: message system is required to sent user a message
        # display all of the order information
        render(request, "Market/cartSent.html", {'orderlist': orderList})
    elif request.method == "GET":
        # return order list and a form for user to fill sentTo
        user = request.user
        orderList = Cart.objects.get(user=user)
        render(request, )


# API view
@csrf_exempt
def apithinglist(request):
    if request.method == 'GET':
        things = Thing.objects.all()
        serializer = ThingSerializer(things, many=True)
        return JsonResponse(serializer.data, safe=False)
