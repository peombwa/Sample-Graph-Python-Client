# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphmultiValueLegacyExtendedProperty(Model):
    """MicrosoftgraphmultiValueLegacyExtendedProperty.

    :param id:
    :type id: str
    :param value:
    :type value: list[str]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'value': {'key': 'value', 'type': '[str]'},
    }

    def __init__(self, id=None, value=None):
        super(MicrosoftgraphmultiValueLegacyExtendedProperty, self).__init__()
        self.id = id
        self.value = value
