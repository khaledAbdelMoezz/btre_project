from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import bedroom_choices, price_choices, state_choices
# Create your views here.

def index (request):

    #all_obj = Listing.objects.all()
    #all_obj = Listing.objects.get_queryset().order_by('price')  # by 'id' or 'realtor'


    all_obj = Listing.objects.order_by('-list_date').filter(is_published = True)   # dont forget the -->  '-'

    paginator = Paginator(all_obj, 3)     # Show 3 Objects per page

    page = request.GET.get ('page')

    paged_obj = paginator.get_page (page)


    context = {'listings': paged_obj }

    return render (request, 'listings/listings.html', context)







def listing (request,id):

    obj = get_object_or_404(Listing, pk = id)
    context = {'obj':obj}
    return render (request,'listings/listing.html',context)









def search (request):

    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords  search
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
    if keywords:
        queryset_list = queryset_list.filter(discription__icontains = keywords)

    # city  search
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact = city)




    # state  search
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact = state)


    # bedrooms  search
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte = bedrooms)

    # Price  search
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte = price)


    context = {
                'bedroom_choices':bedroom_choices,
                'price_choices' : price_choices,
                'state_choices': state_choices,
                'listings':queryset_list,
                'request_values':request.GET              # to keep the search keyword in the search field
                }

    return render (request, 'listings/search.html', context)






























#
