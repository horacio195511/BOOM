from django.shortcuts import render
from Market.models import Thing


# Create your views here.


def createThing(request):
    if request.method == "GET":
        return render(request, 'Market/createThing.html')
    elif request.method == "POST":
        thing = Thing(name=request.POST['name'], file=request.FILES['file'])
        thing.save()
        return render(request, 'Action/success.html', {'action': 'create thing'})


def market(request):
    if request.method == "GET":
        things = []
        for a in range(0, 5):
            things.append(Thing.objects.get(pk=(a + 1)))
        return render(request, 'Market/market.html', {'thing_list': things})
