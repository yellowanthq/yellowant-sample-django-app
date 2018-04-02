### YA Message Button Builders ###
from yellowant.messageformat import MessageButtonsClass


def update_item_button(item, user_integration, text="Update", value=0, name=0):
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