from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
# authenticate = if checks if username or password are correct
# Create your views here.

def index(request):
    # the request object that gets passed in as part of the request
    # to every user in django automatically has a user atttribute associated with it.
    # and that user object has an is_autheticated attribute that tells us
    # if the user is signed in or not.
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
        
    return render(request, "users/user.html")    

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # authenticate is the function whic takes the request
        # if the username and password are valid it'll give me back the user in user variable
        user = authenticate(request, username=username, password=password)
        # if user is not None that means the authentication is successful
        # and i can go ahead and log the user in
        if user is not None:
            # login function which django gives us to log the user in
            # takes request and user which we got from authenticate function
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html",{
                "message": "Invalid credentials"
            })   
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return render(request, "users/login.html",{
        "message": "Logged out."
    })    