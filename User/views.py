from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from CMS.models import NEWS
from User.models import Customer


# Create your views here.


def home(request):
    if request.method == 'GET':
        news_set = []
        # query for news
        for news in NEWS.objects.all():
            news_set.append(news)
        context = {'news_list': news_set[-3:]}
        # TODO: but the image won't display here.
        return render(request, 'home.html', context)


def register(request):
    if request.method == 'GET':
        return render(request, 'User/register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        image = request.FILES['image']
        user = User.objects.create_user(username, email, password, image)
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
