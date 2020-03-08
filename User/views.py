from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from CMS.models import NEWS


# Create your views here.


def home(request):
    if request.method == 'GET':
        news = []
        # query for news
        for a in range(0, 3):
            # TODO: we get the last three news from database is a better implementation.
            news.append(NEWS.objects.get(pk=(a + 1)))
        context = {'news_list': news}
        return render(request, 'home.html', context)


def register(request):
    if request.method == 'GET':
        return render(request, 'User/register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.save()
        return render(request, 'Action/success.html', {'action': 'register'})


def mlogin(request):
    if request.method == 'GET':
        return render(request, 'User/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'Action/success.html', {'action': 'login'})
        else:
            return render(request, 'User/login.html', {'message': 'wrong password or username'})
