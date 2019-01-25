from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Item, Donation
from appprofile.models import Profile

# Create your views here.
def donatenow(request):
    if request.user.is_authenticated:
        items = Item.objects.filter(status=True)
        context = {
            'message': 'Kindly enter the details to donate an item',
            'items': items
        }
        return render(request, 'donate_now.html', context)
    else:
        return HttpResponseRedirect('/auth')

def donate(request):
    if request.method == 'POST':
        item = request.POST['item'][0]
        quantity = request.POST['quantity'][0]
        condition = request.POST['condition'][0]
        description = request.POST['description'][0]
        req_profile = Profile.objects.get(user=request.user)
        req_item = Item.objects.get(pk=item)
        donation = Donation(profile=req_profile, item=req_item, description=description, quantity=quantity, item_condition=condition)
        donation.save()
        items = Item.objects.filter(status=True)
        context = {
            'message': 'Donation record added successfully, a valunteer will pick up the items from your doorsteps.',
            'items': items
        }
        return render(request, 'donate_now.html', context)
    else:
        return HttpResponseRedirect('/donate/now')