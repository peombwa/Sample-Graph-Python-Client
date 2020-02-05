# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphmobileAppSupportedDeviceType(Model):
    """mobileAppSupportedDeviceType.

    :param type: Possible values include: 'desktop', 'windowsRT', 'winMO6',
     'nokia', 'windowsPhone', 'mac', 'winCE', 'winEmbedded', 'iPhone', 'iPad',
     'iPod', 'android', 'iSocConsumer', 'unix', 'macMDM', 'holoLens',
     'surfaceHub', 'androidForWork', 'androidEnterprise', 'blackberry', 'palm',
     'unknown'
    :type type: str or ~users.models.enum
    :param minimum_operating_system_version: Minimum OS version
    :type minimum_operating_system_version: str
    :param maximum_operating_system_version: Maximum OS version
    :type maximum_operating_system_version: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'minimum_operating_system_version': {'key': 'minimumOperatingSystemVersion', 'type': 'str'},
        'maximum_operating_system_version': {'key': 'maximumOperatingSystemVersion', 'type': 'str'},
    }

    def __init__(self, type=None, minimum_operating_system_version=None, maximum_operating_system_version=None):
        super(MicrosoftgraphmobileAppSupportedDeviceType, self).__init__()
        self.type = type
        self.minimum_operating_system_version = minimum_operating_system_version
        self.maximum_operating_system_version = maximum_operating_system_version
