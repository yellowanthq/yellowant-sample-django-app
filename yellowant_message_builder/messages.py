"""YA Message builder"""
from yellowant.messageformat import MessageClass

from .attachments import item_attachment


def items_message(todo_list, user_integration, message=None):
    """Build a YellowAnt message for a list of todo items.

    Args:
        todo_list (list): List of todo items.
        user_integration (yellowant_api.models.UserIntegration): User integration data.
        message (MessageClass, optional): Message to add details to.

    Returns:
        MessageClass: A message containing details about the list of todo items.
    """
    print(todo_list)
    message = message or MessageClass()
    for item in todo_list:
        message.attach(item_attachment(item, user_integration))

    return message


def item_message(item, user_integration, message=None):
    """Build a YellowAnt message from a single todo item.

    Args:
        item (dict): A todo item's data.
        user_integration (yellowant_api.models.UserIntegration): User integration data.
        message (MessageClass, optional): Message to add details to.

    Returns:
        MessageClass: A message containing details about a single todo item.
    """
    message = message or MessageClass()
    message.attach(item_attachment(item, user_integration))
    return message
