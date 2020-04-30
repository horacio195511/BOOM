from django.shortcuts import render
from Market.models import Thing


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
        return render(request, 'Market/createOrder.html')
    elif request.method == 'POST':
        # TODO: store the order into cookie
        # TODO: create order state system.
        pk = request.POST[thingpk]


def confirmOrder(request):
    if request.method == 'GET':
        return render(request, 'Market/confirmOrder.html')
    elif request.method == 'POST':
