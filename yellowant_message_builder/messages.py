"""YA Message builder"""
from yellowant.messageformat import MessageClass

from .attachments import item_attachment


def items_message(todo_list, user_integration, message=None):
    print(todo_list)
    message = message or MessageClass()
    for item in todo_list:
        message.attach(item_attachment(item, user_integration))
    
    return message

def item_message(item, user_integration, message=None):
    message = message or MessageClass()
    message.attach(item_attachment(item, user_integration))
    return message