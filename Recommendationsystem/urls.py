"""Recommendationsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import index
##from . import UserDashboard
##from . import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index.index, name='index'),
    path('about/', index.about, name='about'),
    path('team/', index.team, name='team'),
    path('login/', index.login, name='login'),
    path('dologin/', index.dologin, name='dologin'),
    path('registration/', index.registration, name='registration'),
    path('Reg/', index.Reg, name='Reg'),
    path('AdminLogin/', index.AdminLogin, name='AdminLogin'), 
    path('AdminDashboard/', index.AdminDashboard, name='AdminDashboard'),
    path('Add_Food/', index.Add_Food, name='Add_Food')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

