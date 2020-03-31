from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from CMS.models import NEWS
from User.models import Customer
from Market.models import Thing
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
        double_password = request.POST['double_password']
        image = request.FILES['image']
        if password == double_password:
            base_user = User.objects.create_user(username, email, password)
            base_user.save()
            base_user = User.objects.get(username=username)
            user = Customer(base_user, image)
            user.save()
            return render(request, 'Action/success.html', {'action': 'register'})
        else:
            return render(request, 'User/register.html', {'op_error': 'invalidate second password'})


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


def profile(request):
    if request.method == 'GET':
        user = request.user
        username = user.username
        userimage = user.image
        things = Thing.object.get(owner=user)
        return render(request, 'User/profile.html')
