"""Sample models for the Todo list application"""
from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    """Todo Item

    Attributes:
        title (str): Header title to summarize the todo item.
        description (int): Detailed description of the todo item.
    """
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class UserTodo(models.Model):
    """Todo Owner Relationship

    Attributes:
        user (User): Owner of the todo item.
        todo (Todo): The todo item.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.user.username, self.todo.title) #pylint: disable=no-member
