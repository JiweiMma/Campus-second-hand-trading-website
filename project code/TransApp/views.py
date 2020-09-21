import json
import os
import random
from django.shortcuts import render
from TransApp import models
using=[]
def search(request):
    state = []
    price = []
    des = []
    try:
        if request.method == "POST":
            sellname = request.POST.get("search",None)
        sell=models.sell.objects.filter(state=sellname)
        for i in sell:
            state.append(i.state)
            price.append(i.price)
            des.append(i.description)
    except:
        pass
    return render(request,'search1.html',{'user':json.dumps(using),'state':json.dumps(state),'price':json.dumps(price),'des':json.dumps(des)})
def sell(request):
    return render(request,'sell.html',{'user':json.dumps(using)})
def index(request):
    del using[:]
    state=[]
    price=[]
    des=[]
    for i in models.sell.objects.all():
        state.append(i.state)
        price.append(i.price)
        des.append(i.description)
    return render(request, 'index.html',{'state':json.dumps(state),'price':json.dumps(price),'des':json.dumps(des)})
def register(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        models.user.objects.create(name=username, password=password)
        models.user.save
    return render(request,'register.html')
def index1(request):
    with open(os.getcwd()+'\\user.txt','r') as f:
        using.append(f.read())
    state = []
    price = []
    des = []
    for i in models.sell.objects.all():
        state.append(i.state)
        price.append(i.price)
        des.append(i.description)
    return render(request,'index1.html',{'user':json.dumps(using),'state':json.dumps(state),'price':json.dumps(price),'des':json.dumps(des)})
def add(request):
    if request.method == "POST":
        state = request.POST.get("name", None)
        price = request.POST.get("price", None)
        description = request.POST.get("description",None)
        models.sell.objects.create(state=state,price=price,description=description)
        models.sell.save
        try:
            us = models.user.objects.get(name=using[0])
            se = models.sell.objects.get(state=state)
            models.sellbag.objects.create(user_num=us.id,sell_num=se.id)
            models.sellbag.save
            state = []
            price = []
            des = []
            for i in models.sell.objects.all():
                state.append(i.state)
                price.append(i.price)
                des.append(i.description)
            return render(request,'index1.html',{'user':json.dumps(using),'state':json.dumps(state),'price':json.dumps(price),'des':json.dumps(des)})
        except:
            pass
def delete(request):
    if request.method == "POST":
        shopping=request.POST.get("info",None)
        list_shop=shopping.split(' ')
        shop = models.sell.objects.get(state=list_shop[0])
        models.shoppingcart.objects.get(sell_num=shop.id).delete()
        return render(request,'index1.html',{'user':json.dumps(using)})
def deleteuser(request):
    if request.method == "POST":
        user_info=request.POST.get("info",None)
        user_id=user_info.split(' ')
        try:
            models.user.objects.get(id=user_id[0]).delete()
        except:
            pass
        try:
            models.shoppingcart.objects.get(user_num=user_id[0]).delete()
        except:
            pass
        try:
            models.sellbag.objects.get(user_num=user_id[0]).delete()
        except:
            pass
    id = []
    name = []
    for i in models.user.objects.all():
        id.append(i.id)
        name.append(i.name)
    return render(request, 'manage.html', {'id': json.dumps(id), 'name': json.dumps(name)})
def manage(request):
    id=[]
    name=[]
    for i in models.user.objects.all():
        id.append(i.id)
        name.append(i.name)
    return render(request, 'manage.html', {'id': json.dumps(id),'name':json.dumps(name)})
def cart(request):
    state = []
    price = []
    des = []
    try:
        us = models.user.objects.get(name=using[0])
        sellbag=models.shoppingcart.objects.filter(user_num=us.id)
        for i in sellbag:
            sell=models.sell.objects.get(id=i.sell_num)
            state.append(sell.state)
            price.append(sell.price)
            des.append(sell.description)
    except:
        pass
    return render(request, 'cart.html', {'user': json.dumps(using),'state':json.dumps(state),'price':json.dumps(price),'des':json.dumps(des)})
def addcart(request):
    if request.method == "POST":
        shopping=request.POST.get("info",None)
        list_shop=shopping.split(' ')
        shop=models.sell.objects.get(state=list_shop[0])
        us = models.user.objects.get(name=using[0])
        models.shoppingcart.objects.create(user_num=us.id,sell_num=shop.id)
        return render(request,'index1.html',{'user':json.dumps(using)})
def login(request):
    userName = request.POST.get("username", None)
    userPwd = request.POST.get("password", None)
    if userName=='wcg' and userPwd=='111':
        id = []
        name = []
        for i in models.user.objects.all():
            id.append(i.id)
            name.append(i.name)
        return render(request, 'manage.html', {'id': json.dumps(id), 'name': json.dumps(name)})
    try:
        us=models.user.objects.get(name=userName)
    except:
        success = [0]
        return render(request, 'login.html', {'Success': json.dumps(success)})
    if us.password == userPwd:
        state = []
        price = []
        des = []
        for i in models.sell.objects.all():
            state.append(i.state)
            price.append(i.price)
            des.append(i.description)
        with open(os.getcwd()+'\\user.txt','w') as f:
            f.write(userName)
        using.append(userName)
        using.append(userPwd)
        return render(request,'index1.html',{'user':json.dumps(using),'state':json.dumps(state),'price':json.dumps(price),'des':json.dumps(des)})
    else:
        success=[0]
        return render(request,'login.html',{'Success':json.dumps(success)})
# Create your views here.
