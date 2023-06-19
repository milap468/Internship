from django.shortcuts import render,HttpResponseRedirect,reverse
from django.contrib import messages
from .models import User
from django.contrib.auth import login,logout,authenticate
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def user_register(request):

    if request.method == "POST":

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if first_name=="" or last_name=="" or email=="" or password1=="" or password2=="":
            messages.warning(request, f"You have not enetered your all credentials ...")
            return HttpResponseRedirect(reverse('user-register'))
        
        if password1 != password2:
            messages.warning(request,"Your Passwords are not Matched. Please Enter them correctly.")
            return HttpResponseRedirect(reverse('user-register'))
        
        if "@" not in email:
            messages.warning(request,"Enter Valid Email Address...")
            return HttpResponseRedirect(reverse('user-register'))
        
        user = User.objects.create(first_name=first_name,last_name=last_name,email=email,password=password1)
        user.set_password(password1)
        user.save()

        return HttpResponseRedirect(reverse("user-login"))

    return render(request,'accounts/user-register.html')

def user_login(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(email=email,password=password)

        if user:
            login(request,user)

            return HttpResponseRedirect(reverse("index"))
        else:
            messages.warning(request,"Your Have to Enter the valid Credentials...")
            return HttpResponseRedirect(reverse('user-login'))

    return render(request,"accounts/user-login.html")

def user_logout(request):

    logout(request)

    return HttpResponseRedirect(reverse("user-login"))




def forgot_password(request):

    try:
        if request.method == "POST":

            email = request.POST.get('email')

            send_mail(
            "Password reset message...",
            f"Please do not share this link with anyone. http://127.0.0.1:8000/accounts/change-password/{email}",
            'patelmilap89@gmail.com',
            [email],
            fail_silently=False,
            )
    except:
        return HttpResponseRedirect(reverse("user-login"))
    
    return HttpResponseRedirect(reverse("user-login"))
        

