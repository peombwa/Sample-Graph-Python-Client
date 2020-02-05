# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphalternativeSecurityId(Model):
    """alternativeSecurityId.

    :param type:
    :type type: int
    :param identity_provider:
    :type identity_provider: str
    :param key:
    :type key: bytes
    """

    _validation = {
        'type': {'maximum': 2147483647, 'minimum': -2147483648},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'int'},
        'identity_provider': {'key': 'identityProvider', 'type': 'str'},
        'key': {'key': 'key', 'type': 'base64'},
    }

    def __init__(self, type=None, identity_provider=None, key=None):
        super(MicrosoftgraphalternativeSecurityId, self).__init__()
        self.type = type
        self.identity_provider = identity_provider
        self.key = key