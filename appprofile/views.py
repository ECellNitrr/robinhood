from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

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
    if request.user.is_authenticated:
        return HttpResponseRedirect('/donate/now')
    return render(request, 'auth.html')

def auth_logout(request):
    logout(request)
    return render(request, 'auth.html')

def create_account(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        contact_no = request.POST['contact_no']
        user = User.objects.create_user(email, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.profile.contact_no = contact_no
        user.save()
    return HttpResponseRedirect('/auth')

def account_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/donate/now')        
    return HttpResponseRedirect('/auth')