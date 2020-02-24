from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World, this is my first view response')

# Create your views here.
