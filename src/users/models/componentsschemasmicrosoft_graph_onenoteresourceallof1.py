# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphOnenoteresourceallof1(Model):
    """onenoteResource.

    :param content:
    :type content: bytes
    :param content_url:
    :type content_url: str
    """

    _attribute_map = {
        'content': {'key': 'content', 'type': 'base64'},
        'content_url': {'key': 'contentUrl', 'type': 'str'},
    }

    def __init__(self, content=None, content_url=None):
        super(ComponentsschemasmicrosoftGraphOnenoteresourceallof1, self).__init__()
        self.content = content
        self.content_url = content_url