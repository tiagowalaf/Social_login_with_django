from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout

def home(request):
    return render(request, 'account/login.html')

def congrats(request):
    return HttpResponse(f'You are loged in {request.user}')

def logoutuser(request):
    logout(request)
    return redirect('/')