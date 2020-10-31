from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from CMS.models import NEWS
from Market.models import Thing
from BOOM.modelform import LoginForm, RegisterForm
from Printer.models import Printer
from User.models import Customer


def home(request):
    if request.method == 'GET':
        news_set = []
        # query for news
        for news in NEWS.objects.all():
            news_set.append(news)
        context = {'news_list': news_set[-3:]}
        return render(request, 'home.html', context)


def usercreate(request):
    if request.method == 'GET':
        form = RegisterForm()
        context = {'title': 'User-Register',
                   'form': form,
                   'submitTitle': 'Register'}
        return render(request, 'Form.html', context)
    elif request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        form.save()
        return render(request, 'Action/success.html', {'action': 'user create'})


def userlogin(request):
    if request.method == 'GET':
        form = LoginForm()
        context = {'title': 'User-Login',
                   'form': form,
                   'submitTitle': 'Login'}
        return render(request, 'Form.html', context)
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'Action/success.html', {'action': 'user login'})
        else:
            return redirect('/userlogin/')


def userlogout(request):
    logout(request)
    return render(request, 'Action/success.html', {'action': 'logout'})


def userprofile(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            user = request.user
            userimage = user.customer.image
            thing_list = Thing.objects.filter(owner=user)
            printer_list = Printer.objects.filter(owner=user)
            return render(request, 'User/profile.html',
                          {'user': user, 'userimage': userimage, 'thing_list': thing_list,
                           'printer_list': printer_list})
        else:
            return redirect('/login/')
