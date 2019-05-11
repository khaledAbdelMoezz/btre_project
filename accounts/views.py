from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from contacts.models import Contact

def register_user(request):

    if request.method == 'POST':

        # get the form Data

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request,'That Username Has Been Taken !')
                return redirect ('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request,'That Email Is Being Used !')
                    return redirect ('register')
                else:
                    user = User.objects.create_user(first_name = first_name,
                    last_name = last_name, username = username, email = email,
                    password = password)

                    #login(request,user)
                    #messages.success(request, ' Registeration Was Successful')
                    #return redirect ('index')
                    user.save()
                    messages.success(request, ' Registeration Was Successful, You Can Log-In Hier !')
                    return redirect ('login')
        else:
            messages.error(request,'Password Do Not Match')
            return redirect ('register')

    else:
        return render(request,'accounts/register.html')









def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate (request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, ' You Are Logged In !')
            return redirect ('dashboard')
        else:
            messages.error(request,' Username Or Password Is Not Correct !')
            return redirect ('login')
    else:
        return render(request,'accounts/login.html',{})





def logout_user(request):
    logout(request)
    messages.success(request,'YOU ARE LOGGED-OUT ..See You Soon !')
    return redirect('index')




@login_required
def dashboard(request):

    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id = request.user.id)
    context = {'contacts': user_contacts }
    return render(request,'accounts/dashboard.html',context)
