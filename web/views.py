"""Views for the web clients"""
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from yellowant_api.models import UserIntegration


def index(request):
    """Display home page.
    """
    context = {
        "user_integrations": []
    }

    if request.user.is_authenticated:
        user_integrations = UserIntegration.objects.filter(user=request.user)
        for user_integration in user_integrations:
            context["user_integrations"].append(user_integration)

    return render(request, "home.html", context)


def signup(request):
    """Handle sign up and display sign up form.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        print("invalid")
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
