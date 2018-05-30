"""YA Message Button Builders"""
from yellowant.messageformat import MessageButtonsClass


def update_item_button(item, user_integration, text="Update", value=0, name=0):
    """Create a YellowAnt message attachment button to update todo item.

    Args:
        item (dict): Todo item data.
        user_integration (yellowant_api.models.UserIntegration): User integration data.
        text (str): Button text.
        value (int): Useless.
        name (int): Useless.

    Returns:
        MessageButtonsClass: A YellowAnt message attachment button which allows users to update an
            item.
    """
    button = MessageButtonsClass()
    button.text = text
    button.value = value
    button.name = name

    button.command = {
        "function_name": "updateitem",
        "service_application": user_integration.yellowant_integration_id,
        "data": {
            "id": item.get("id")
        },
        "inputs": [
            "title",
            "description"
        ]
    }

    return button
