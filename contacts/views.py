from django.shortcuts import render, redirect, reverse
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == "POST":

        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id

            has_contacted = Contact.objects.all().filter(listing_id = listing_id, user_id = user_id)
            if has_contacted:
                messages.error(request, ' Your have already made an inquiry for theis Object ')
                return redirect ('/listings/' + listing_id )


        contact = Contact(listing =listing,listing_id = listing_id,
        name = name, email = email, phone = phone, message = message,
        user_id = user_id )

        contact.save()

        send_mail('WE RECIEVED YOUR INQUIRY','Here is the Confirmation.','khaled.a.moezz@gmail.com',
        [email, realtor_email],fail_silently=False)


        messages.success (request, 'THANK YOU! Your inquery has been Send!')
        return redirect ('/listings/' + listing_id )
