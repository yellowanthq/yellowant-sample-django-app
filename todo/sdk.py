"""Fake SDK to manipulate user todos"""
from django.forms.models import model_to_dict
from django.contrib.auth.models import User

from .models import Todo, UserTodo


class TodoSDK:
    """Todo SDK
    
    Args:
        token (int): sdk auth token from the client. Right now user id is the same as the token.
    """
    def __init__(self, token):
        self.user = User.objects.get(id=token)
    
    def create_item(self, title, description=None):
        todo = Todo(title=title, description=description)
        todo.save()

        user_todo = UserTodo(user=self.user, todo=todo)
        user_todo.save()

        return model_to_dict(todo)
    
    def get_list(self):
        user_todo_list = UserTodo.objects.filter(user=self.user)
        todo_list = []

        for user_todo in user_todo_list:
            todo_list.append(user_todo.todo)
        
        return list(map(model_to_dict, todo_list))
    
    def get_item(self, id):
        todo = UserTodo.objects.get(user=self.user, todo=id).todo

        return model_to_dict(todo)
    
    def update_item(self, id, title=None, description=None):
        todo = UserTodo.objects.get(user=self.user, todo=id).todo

        todo.title = title or todo.title
        todo.description = description or todo.description
        todo.save()

        return model_to_dict(todo)
    
    def delete_item(self, id):
        todo = UserTodo.objects.get(user=self.user, todo=id).todo
        todo.delete()

        return self.get_list()