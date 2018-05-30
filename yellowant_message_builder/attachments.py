""" YA Message Attachment Builders """
from yellowant.messageformat import MessageAttachmentsClass, AttachmentFieldsClass

from .buttons import update_item_button


def item_attachment(item, user_integration, attachment=None):
    """YellowAnt message attachment to show an item's details.

    Args:
        item (dict): Item data.
        user_integration (yellowant_api.models.UserIntegration): User integration data.
        attachment (MessageAttachmentsClass, optional): Attachment to add details to.

    Returns:
        MessageAttachmentsClass: An attachment with the todo details and actions to update it.
    """
    attachment = attachment or MessageAttachmentsClass()
    attachment.title = item.get("title")
    attachment.text = item.get("description")

    attachment.attach_field(AttachmentFieldsClass("ID", 1, item.get("id")))

    attachment.attach_button(update_item_button(item, user_integration))

    return attachment
