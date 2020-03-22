from django.shortcuts import render
from Market.models import Thing


# Create your views here.


def createThing(request):
    if request.method == "GET":
        return render(request, 'Market/createThing.html')
    elif request.method == "POST":
        # TODO: the user must log in first to create thing
        thing = Thing(name=request.POST['name'], file=request.FILES['file'], image=request.FILES['image'],
                      owner=request.user)
        thing.save()
        return render(request, 'Action/success.html', {'action': 'create thing'})


def market(request):
    if request.method == "GET":
        things = []
        for thing in Thing.object.all():
            things.append(thing)
        return render(request, 'Market/market.html', {'thing_list': things[-7:]})
