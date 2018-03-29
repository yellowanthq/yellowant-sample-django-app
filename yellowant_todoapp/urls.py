"""yellowant_todoapp URL Configuration"""
from django.urls import include, path
from django.contrib import admin
from django.views.generic.base import TemplateView

from todo import urls as todo_urls
from web import urls as web_urls

urlpatterns = [
    path('', include(web_urls)),
    path("accounts/", include('django.contrib.auth.urls')),
    path("admin/", admin.site.urls),
    path("api/", include(todo_urls)),
]
