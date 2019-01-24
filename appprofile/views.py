from django.shortcuts import render

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