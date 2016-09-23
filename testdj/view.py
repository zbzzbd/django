# -*- coding:utf-8 -*-

#from django.http import  HttpResponse
from django.shortcuts import render

def hello(request):
    context ={}
    context['hello']='hello zbz!'
    return render(request,'hello.html',context)

def add(request):
    context={}

    a = request.GET['number1']
    b = request.GET['number2']
    a = int(a)
    b = int(b)
    context['c'] =a+b
    return render(request,'index.html',context)
