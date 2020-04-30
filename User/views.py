from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from CMS.models import NEWS
from User.models import Customer


def home(request):
    if request.method == 'GET':
        news_set = []
        # query for news
        for news in NEWS.objects.all():
            news_set.append(news)
        context = {'news_list': news_set[-3:]}
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
            customer = Customer(user_id=base_user.id, image=image)
            customer.save()
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
            return redirect('/login/')


def mlogout(request):
    logout(request)
    return render(request, 'Action/success.html', {'action': 'logout'})


def profile(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            user = request.user
            userimage = user.customer.image
            return render(request, 'User/profile.html', {'user': user, 'userimage': userimage})
        else:
            return redirect('/login/')
