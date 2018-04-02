### YA Message Attachment Builders ###
from yellowant.messageformat import MessageAttachmentsClass, AttachmentFieldsClass

from .buttons import update_item_button


def item_attachment(item, user_integration, attachment=None):
    attachment = attachment or MessageAttachmentsClass()
    attachment.title = item.get("title")
    attachment.text = item.get("description")

    attachment.attach_field(AttachmentFieldsClass("ID", 1, item.get("id")))

    attachment.attach_button(update_item_button(item, user_integration))

    return attachment