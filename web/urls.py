from django.urls import path

from web.views import index


urlpatterns = [
    path("", index, name="home"),
]