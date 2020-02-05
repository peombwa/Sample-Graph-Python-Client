# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphitemBody(Model):
    """itemBody.

    :param content_type: Possible values include: 'text', 'html'
    :type content_type: str or ~users.models.enum
    :param content:
    :type content: str
    """

    _attribute_map = {
        'content_type': {'key': 'contentType', 'type': 'str'},
        'content': {'key': 'content', 'type': 'str'},
    }

    def __init__(self, content_type=None, content=None):
        super(MicrosoftgraphitemBody, self).__init__()
        self.content_type = content_type
        self.content = content