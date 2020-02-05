# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Microsoftgraphthumbnail(Model):
    """thumbnail.

    :param content:
    :type content: bytes
    :param height:
    :type height: int
    :param source_item_id:
    :type source_item_id: str
    :param url:
    :type url: str
    :param width:
    :type width: int
    """

    _validation = {
        'height': {'maximum': 2147483647, 'minimum': -2147483648},
        'width': {'maximum': 2147483647, 'minimum': -2147483648},
    }

    _attribute_map = {
        'content': {'key': 'content', 'type': 'base64'},
        'height': {'key': 'height', 'type': 'int'},
        'source_item_id': {'key': 'sourceItemId', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'width': {'key': 'width', 'type': 'int'},
    }

    def __init__(self, content=None, height=None, source_item_id=None, url=None, width=None):
        super(Microsoftgraphthumbnail, self).__init__()
        self.content = content
        self.height = height
        self.source_item_id = source_item_id
        self.url = url
        self.width = width