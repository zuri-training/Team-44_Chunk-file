from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View

# Create your views here.

# Registration view


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username):
            messages.error(request, "Username Already Exist")
            return redirect("register")

        if User.objects.filter(email=email):
            messages.error(request, "Email Already Exist")
            return redirect("register")

        user = User.objects.create_user(username, email, password)
        user.save()

        messages.success(request, "Your account has been successfully created")
        return redirect("login")

    return render(request, 'accounts/reg_form.html')

# login View


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, "Invalid Credential")
            return redirect("login")
    return render(request, "accounts/login.html")
