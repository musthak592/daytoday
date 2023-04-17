from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from django.contrib.auth.models import User, auth
from django.contrib import messages


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid details')
            return redirect('rll:login')
    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('rll:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('rll:register')
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save();
                print("user created")
                return redirect('sapp:shop')
        else:
            print("password not match")
            return redirect('registration.html')
    else:
        return render(request, "registration.html")
