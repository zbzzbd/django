# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import  HttpResponse
# Create your views here.

def add(request):
     a =request.GET['a']
     b = request.GET['b']
     c = int(a)+int(b)
     return HttpResponse(str(c))

def add2(request, a, b):
    c =int(a)+int(b)
    return HttpResponse(str(c))

def index(request):
    return render(request,'home.html')

def string(request):
    stringlist=["html","css","jquery","python","Django"]
    context={}
    context['stringlist']=stringlist
    context['dict']={'content':'zbz','site':'localhost'}
    context['list']=map(str,range(100))
    return render(request,'string.html',context)