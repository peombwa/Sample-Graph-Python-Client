# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphwebPart(Model):
    """webPart.

    :param type:
    :type type: str
    :param data:
    :type data: object
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'data': {'key': 'data', 'type': 'object'},
    }

    def __init__(self, type=None, data=None):
        super(MicrosoftgraphwebPart, self).__init__()
        self.type = type
        self.data = data