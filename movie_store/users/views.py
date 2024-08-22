from django.shortcuts import render,redirect
from django.contrib.auth.models import User#user model
from django.contrib.auth import authenticate,login,logout



def userlogin(request):
    error_message= None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)

        if user:
            login(request,user)
            return redirect("home")
        else:
            error_message='Invalid credentials'

    return render (request,"users/login.html",{"error_message":error_message})

def signup(request):
    user=None
    error_message=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=User.objects.create_user(username=username,password=password)
            return redirect("login")
        except Exception as e:
            error_message=str(e)

    return render(request,'users/create.html',{"user":user,"error_message":error_message})


def userlogout(request):
    logout(request)
    return redirect("login")

