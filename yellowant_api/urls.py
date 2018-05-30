"""Urls for YellowAnt related API"""
from django.urls import path

from .views import request_yellowant_oauth_code, yellowant_oauth_redirect, yellowant_api


urlpatterns = [
    path("create-new-integration/", request_yellowant_oauth_code,
         name="request-yellowant-oauth"),
    path("yellowant-oauth-redirect/", yellowant_oauth_redirect,
         name="yellowant-oauth-redirect"),
    path("yellowant-api/", yellowant_api, name="yellowant-api"),
]
