# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphvisualProperties(Model):
    """visualProperties.

    :param title:
    :type title: str
    :param body:
    :type body: str
    """

    _attribute_map = {
        'title': {'key': 'title', 'type': 'str'},
        'body': {'key': 'body', 'type': 'str'},
    }

    def __init__(self, title=None, body=None):
        super(MicrosoftgraphvisualProperties, self).__init__()
        self.title = title
        self.body = body