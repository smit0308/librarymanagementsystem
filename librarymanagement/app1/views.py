from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from app1.models import librarian, reader
from django.contrib import auth
from librarymanagement import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            auth_login(request, user)
            return redirect('/')  
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, 'login.html', {'login_failed': True},'Invalid user or password')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        
        x = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
        x.save()
        
        reader_instance = reader.objects.create(
            user=x,
            user_name=username,
            first_name=firstname,
            last_name=lastname,
            email=email
        )
        reader_instance.save()
        print("Patient created successfully")
      
        return redirect('/')
    else:
        return render(request, 'register.html')
    
def registerform(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        address = request.POST['address']
        contact = request.POST['contact']
        pic_upload = request.FILES['pic_upload']

        user = request.user


        reader_instance = reader.objects.get(user=user)
        reader_instance.full_name = full_name
        reader_instance.address = address
        reader_instance.contact = contact
        reader_instance.save()

        print("Reader updated successfully")
        return redirect('/')
    else:
        return render(request, 'registerform.html')
    