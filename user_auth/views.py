from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse


# Create your views here.
def user_login(request):
    """
    Requests the authentication/login.html page be loaded
    """
    return render(request, 'authentication/login.html')


def authenticate_user(request):
    """
    Requests a user object from the server based on the username and password entered.
    If one exists the user is logged in and returned to the home page, if not they are
    returned to the login page.
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('home:home')
        )


# I followed this guide for creating a simple registration form -
# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
def register_user(request):
    """
    Allows a new user object to be created using a username and password entered
    into the registration form. This is then posted to the server to be added to
    the database of users.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home:home')
    else:
        form = UserCreationForm()
    return render(request, 'authentication/registration.html', {'form': form})


def logout_view(request):
    """
    Logs a user out and returns them to the home page
    """
    logout(request)
    return redirect('home:home')

