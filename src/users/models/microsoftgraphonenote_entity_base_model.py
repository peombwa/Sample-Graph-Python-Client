# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphonenoteEntityBaseModel(Model):
    """MicrosoftgraphonenoteEntityBaseModel.

    :param id:
    :type id: str
    :param self:
    :type self: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'self': {'key': 'self', 'type': 'str'},
    }

    def __init__(self, id=None, self=None):
        super(MicrosoftgraphonenoteEntityBaseModel, self).__init__()
        self.id = id
        self.self = self
