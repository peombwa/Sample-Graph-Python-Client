# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphSinglevaluelegacyextendedpropertyallof1(Model):
    """singleValueLegacyExtendedProperty.

    :param value:
    :type value: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, value=None):
        super(ComponentsschemasmicrosoftGraphSinglevaluelegacyextendedpropertyallof1, self).__init__()
        self.value = value
