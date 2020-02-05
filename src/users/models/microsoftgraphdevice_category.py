# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphdeviceCategory(Model):
    """MicrosoftgraphdeviceCategory.

    :param id:
    :type id: str
    :param display_name: Display name for the device category.
    :type display_name: str
    :param description: Optional description for the device category.
    :type description: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, id=None, display_name=None, description=None):
        super(MicrosoftgraphdeviceCategory, self).__init__()
        self.id = id
        self.display_name = display_name
        self.description = description
