from django.shortcuts import render
from django.contrib.auth import logout

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def learnmore(request):
    return render(request, 'learnmore.html')

def store(request):
    return render(request, 'store.html')

def donate(request):
    return render(request, 'donate.html')

def auth(request):
    return render(request, 'auth.html')

def auth_logout(request):
    logout(request)
    return render(request, 'auth.html')