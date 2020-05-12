"""BOOM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from User.views import register, mlogin, mlogout, home, profile
from CMS.views import createNews, cms
from Market.views import createThing, market

urlpatterns = [
    re_path(r'register/$', register),
    re_path(r'login/$', mlogin),
    re_path(r'logout/$', mlogout),
    re_path(r'home/$', home),
    re_path(r'market/$', market),
    re_path(r'profile/$', profile),
    re_path('creatething/$', createThing),
    path('admin/', admin.site.urls),
    path('', home),
    path('CMS/', cms),
    path('createnews/', createNews),
]
