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
from User.views import usercreate, userlogin, userprofile, userlogout, home
from CMS.views import newscreate, cms
from Market.views import thingcreate, ordercreate, market, apithinglist
from Printer.views import printercreate

# TODO: the url setting now would infinitely concatethe url in the back, how to make it short?
#   use
urlpatterns = [
    re_path(r'usercreate/$', usercreate, name='boom-register'),
    re_path(r'userlogin/$', userlogin, name='boom-login'),
    re_path(r'userlogout/$', userlogout, name='boom-logout'),
    re_path(r'home/$', home, name='boom-home'),
    re_path(r'market/$', market, name='boom-market'),
    re_path(r'userprofile/$', userprofile, name='boom-profile'),
    re_path(r'thingcreate/$', thingcreate, name='boom-creatething'),
    re_path(r'ordercreate/(?P<thingpk>[0-9]*)/$', ordercreate, name='createorder'),
    re_path(r'printercreate/$', printercreate),
    re_path(r'newscreate/$', newscreate),
    path('admin/', admin.site.urls),
    path('', home),
    # api url
    re_path(r'api/thinglist/$', apithinglist)
    # news, thing, order could be accessed by user
    # re_path(r'api/usercreate/$'),
    # re_path(r'api/userlogin/$'),
    # re_path(r'api/userlogout/$'),
    # re_path(r'api/userprofile/$'),
    # re_path(r'api/userdelete/$'),
    # re_path(r'api/userupdate/$'),
    # re_path(r'api/printercreate/$'),
    # re_path(r'api/printerprofile/$'),
    # re_path(r'api/thingcreate/$'),
    # re_path(r'api/thingdelete/$'),
    # re_path(r'api/thingupdate/$'),
    # re_path(r'api/thingprofile/$'),
    # re_path(r'api/ordercreate/$'),
    # re_path(r'api/ordercancel/$'),
    # re_path(r'api/orderprofile/$'),
    # # news entity should only be accessed by sit manager
    # re_path(r'api/newscreate/$'),
    # re_path(r'api/newsupdate/$'),
    # re_path(r'api/newsdelete/$'),
    # re_path(r'api/newsprofile/$'),
]
