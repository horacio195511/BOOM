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
                      description=request.POST['description'], owner=request.user, price=request.POST['price'])
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
