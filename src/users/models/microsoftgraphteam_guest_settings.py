# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphteamGuestSettings(Model):
    """teamGuestSettings.

    :param allow_create_update_channels:
    :type allow_create_update_channels: bool
    :param allow_delete_channels:
    :type allow_delete_channels: bool
    """

    _attribute_map = {
        'allow_create_update_channels': {'key': 'allowCreateUpdateChannels', 'type': 'bool'},
        'allow_delete_channels': {'key': 'allowDeleteChannels', 'type': 'bool'},
    }

    def __init__(self, allow_create_update_channels=None, allow_delete_channels=None):
        super(MicrosoftgraphteamGuestSettings, self).__init__()
        self.allow_create_update_channels = allow_create_update_channels
        self.allow_delete_channels = allow_delete_channels