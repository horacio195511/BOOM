from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from CMS.models import NEWS
from BOOM.modelform import LoginForm, RegisterForm
from User.models import Customer


def home(request):
    if request.method == 'GET':
        news_set = []
        # query for news
        for news in NEWS.objects.all():
            news_set.append(news)
        context = {'news_list': news_set[-3:]}
        return render(request, 'home.html', context)


def userCreate(request):
    if request.method == 'GET':
        form = RegisterForm()
        context = {'title': 'User-Register',
                   'form': form,
                   'submitTitle': 'Register'}
        return render(request, 'Form.html', context)
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        form.save()
        return render(request, 'Action/success.html', {'action': 'user create'})


def userLogin(request):
    if request.method == 'GET':
        form = LoginForm()
        context = {'title': 'User-Login',
                   'form': form,
                   'submitTitle': 'Login'}
        return render(request, 'Form.html', context)
    elif request.method == 'POST':
        form = LoginForm(request.POST)

        return render(request, 'Action/success.html', {'action': 'user login'})


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
