from django.http import HttpResponse
from django.shortcuts import render

from yellowant_api.models import UserIntegration


def index(request):
    context = {
        "user_integrations": []
    }

    if request.user.is_authenticated:
        user_integrations = UserIntegration.objects.filter(user=request.user)
        for user_integration in user_integrations:
            context["user_integrations"].append(user_integration)

    return render(request, "home.html", context)