"""SchoolTransaction URL Configuration

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
from django.urls import path,re_path
from TransApp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('index/',views.index),
    re_path(r'(?=index.html$)',views.index),
    re_path(r'(?=login/$)',views.login),
    re_path(r'(?=add/$)',views.add),
    re_path(r'(?=login.html$)',views.login),
    re_path(r'(?=register/$)',views.register),
    re_path(r'(?=sell.html$)',views.sell),
    re_path(r'(?=index1.html$)',views.index1),
    re_path(r'(?=index1/$)',views.index1),
    re_path(r'(?=sell/$)',views.sell),
    re_path(r'(?=addto/$)',views.addcart),
    re_path(r'(?=register.html$)',views.register),
    re_path(r'(?=cart.html$)',views.cart),
    re_path(r'(?=delete/$)', views.delete),
    re_path(r'(?=search1.html$)', views.search),
    re_path(r'(?=search1/$)', views.search),
    re_path(r'(?=manage.html$)', views.manage),
    re_path(r'(?=deleteUser/$)', views.deleteuser),
]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
