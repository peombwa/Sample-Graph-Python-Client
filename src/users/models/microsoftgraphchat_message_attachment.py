# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphchatMessageAttachment(Model):
    """chatMessageAttachment.

    :param id:
    :type id: str
    :param content_type:
    :type content_type: str
    :param content_url:
    :type content_url: str
    :param content:
    :type content: str
    :param name:
    :type name: str
    :param thumbnail_url:
    :type thumbnail_url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'content_type': {'key': 'contentType', 'type': 'str'},
        'content_url': {'key': 'contentUrl', 'type': 'str'},
        'content': {'key': 'content', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'thumbnail_url': {'key': 'thumbnailUrl', 'type': 'str'},
    }

    def __init__(self, id=None, content_type=None, content_url=None, content=None, name=None, thumbnail_url=None):
        super(MicrosoftgraphchatMessageAttachment, self).__init__()
        self.id = id
        self.content_type = content_type
        self.content_url = content_url
        self.content = content
        self.name = name
        self.thumbnail_url = thumbnail_url