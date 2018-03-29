from django.urls import path

from .views import create_user, retrieve_destroy_user, list_create_todo, retrieve_update_destroy_todo

urlpatterns = [
    path("user/", create_user, name="create-user"),
    path("user/<int:user>/", retrieve_destroy_user, name="retrieve-destroy-user"),
    path("todo/", list_create_todo, name="list-create-todo"),
    path("todo/<int:todo>/", retrieve_update_destroy_todo, name="retrieve-update-destroy-todo"),
]