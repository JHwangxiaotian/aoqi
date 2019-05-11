from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(request):
    print("==接口被APP请求了==")
    return HttpResponse('这是app对应的数据页面')