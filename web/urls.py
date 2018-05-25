from django.urls import path

from web.views import index, signup


urlpatterns = [
    path("", index, name="home"),
    path("signup/", signup, name="signup")
]