from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World, this is my first view response')

def siddhu(request):
    return HttpResponse('Hello worald')

# Create your views here.

