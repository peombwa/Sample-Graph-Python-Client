# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphinformationProtectionLabel(Model):
    """MicrosoftgraphinformationProtectionLabel.

    :param id:
    :type id: str
    :param name:
    :type name: str
    :param description:
    :type description: str
    :param color:
    :type color: str
    :param sensitivity:
    :type sensitivity: int
    :param tooltip:
    :type tooltip: str
    :param is_active:
    :type is_active: bool
    """

    _validation = {
        'sensitivity': {'maximum': 2147483647, 'minimum': -2147483648},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'color': {'key': 'color', 'type': 'str'},
        'sensitivity': {'key': 'sensitivity', 'type': 'int'},
        'tooltip': {'key': 'tooltip', 'type': 'str'},
        'is_active': {'key': 'isActive', 'type': 'bool'},
    }

    def __init__(self, id=None, name=None, description=None, color=None, sensitivity=None, tooltip=None, is_active=None):
        super(MicrosoftgraphinformationProtectionLabel, self).__init__()
        self.id = id
        self.name = name
        self.description = description
        self.color = color
        self.sensitivity = sensitivity
        self.tooltip = tooltip
        self.is_active = is_active
