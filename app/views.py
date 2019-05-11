from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor

from listings.choices import bedroom_choices, price_choices, state_choices

def index(request):

    obj = Listing.objects.order_by('-list_date').filter(is_published = True)[:3] # just 3 objects

    context = {
                'listings':obj,
                'bedroom_choices':bedroom_choices,
                'price_choices' : price_choices,
                'state_choices': state_choices
                }

    return render(request,'app/index.html', context)

def about(request):

    all_obj = Realtor.objects.order_by('hire_date')
    best_seller = Realtor.objects.order_by('-name').filter(is_mvp = True)

    context = {"listings":all_obj , "best_seller":best_seller}

    return render(request,'app/about.html', context)
