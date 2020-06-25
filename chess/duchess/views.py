from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *

# Create your views here.

    
def play(request):
    return HttpResponse("Play")

def login(request):
    return render(request,'accounts/login.html')

def register(request):
    form = UserCreationForm()

    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/register.html',context)

def home(request):
    games = Game.objects.all()
    return render(request,'play/home.html',{'games':games})