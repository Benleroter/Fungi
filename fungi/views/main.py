from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from fungi.models import Fungi
from fungi.views.filteredfungi import FungiToSearch
from fungi.models import *
from usersettings.models import Show, ShowSearchFields
from django.views.generic import ListView
from django import forms
from fungi.forms import  UserRegisterForm
from django.views import View

from django.contrib.auth.models import AnonymousUser

def home(request):
    if request.user.is_authenticated:
        uid = request.user
        print('uid',uid)
        UserShowSettings = Show.objects.get(user_id= request.user)
    else:
        uid = User.objects.get(username='GuestUser') 
        print('uid',uid)
        UserShowSettings = Show.objects.get(user_id= uid)
    
    context = {
        'fungis' : Fungi.objects.all(),
        }
    return render(request, 'fungi/home.html', context)

def AllFungi(request):
    if request.user.is_authenticated:
        uid = request.user
        UserShowSettings = Show.objects.get(user_id= request.user)
    else:
        uid = User.objects.get(username='GuestUser') 
        UserShowSettings = Show.objects.get(user_id= uid)

    #Show or don't show non-UK Species and/or Macromycetes
    FungiToRender = FungiToSearch(Fungi, UserShowSettings.ShowOnlyUKOccurences, UserShowSettings.ShowMacromycetes)

    context = {
        'fungis' : FungiToRender[0],
        'fungicount' : FungiToRender[1],
        'ResultText' : FungiToRender[2]
        }
    return render(request, 'fungi/allfungi.html', context)


def searchsuccess(request):
	return render(request, 'fungi/search_results.html')

def nosearchresults(request):
    return render(request, 'fungi/nosearchresults.html')    

def about(request):
    return render(request, 'fungi/about.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

