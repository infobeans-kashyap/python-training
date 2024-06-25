from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

def register(request):
    if request.method == 'POST' :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password :
            if User.objects.filter(username=user_name).exists() :
                messages.info(request, 'User name is already taken!!')
                return redirect('signup')
            elif  User.objects.filter(email=email).exists() :
                messages.info(request, 'Email already exists!!')
                return redirect('signup')
            else :
                user = User.objects.create_user(username=user_name, email=email, password=password, first_name=first_name, last_name=last_name)
                user.save()
        else :
            messages.info(request, 'Password and confirm password do not match')
            return redirect('signup')
        return redirect('/')
    else :
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST' :
        user_name = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(username=user_name, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else :
            messages.info(request, 'Invalid credentials!!')
            return render(request, 'signup.html')
    else :
        return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return render(request, 'signup.html')