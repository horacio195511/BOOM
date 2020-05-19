from django.shortcuts import render, redirect
from Market.models import Thing, Order


# Create your views here.


def createThing(request):
    if request.method == "GET":
        # the case which use haven't login
        if request.user.is_authenticated:
            return render(request, 'Market/createThing.html')
        else:
            return render(request, 'User/login.html')
    elif request.method == "POST":
        thing = Thing(name=request.POST['name'], file=request.FILES['file'], image=request.FILES['image'],
                      description=request.POST['description'], owner=request.user)
        thing.save()
        return render(request, 'Action/success.html', {'action': 'create thing'})


def market(request):
    if request.method == "GET":
        things = []
        for thing in Thing.objects.all():
            things.append(thing)
        # TODO: there should be a way to identify the thing user choose in market.
        #   directly use pk of thing is the simplest solution.
        return render(request, 'Market/market.html', {'thing_list': things[-7:]})


def createOrder(request, thingpk):
    # get the thing through the pk of thing
    if request.method == 'GET':
        # TODO: take the primary key of selected object as input, and display according information
        # TODO: because we want to create multiple order in a time so the fronend should be modified
        thing = Thing.objects.get(pk=thingpk)
        return render(request, 'Market/createOrder.html', {'thing': thing})
    elif request.method == 'POST':
        # TODO: store the order into cookie
        # TODO: create order state system.
        pk = request.POST['thingpk']
        cartID = giveID()
        user = request.User
        thing = Thing.objects.get(pk=thingpk)
        amount = request.POST['amount']
        price = amount * Thing.price
        # TODO: create state trace system
        state = 'CREATED'
        # TODO: create order dispatcher, and the order management sytem
        maker = dispatcher()
        order = Order()
        return redirect('/market/')

# def confirmOrder(request):
#     if request.method == 'GET':
#         return render(request, 'Market/confirmOrder.html')
#     elif request.method == 'POST':
