from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world")

def wow(request):
    return HttpResponse("wow")
# Create your views here.
