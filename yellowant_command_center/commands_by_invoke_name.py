"""Mapping for command invoke name to logic"""
from .commands import create_item, get_list, get_item, update_item, delete_item


COMMANDS_BY_INVOKE_NAME = {
    "createitem": create_item,
    "getlist": get_list,
    "getitem": get_item,
    "updateitem": update_item,
    "deleteitem": delete_item,
}
