# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphobjectIdentity(Model):
    """objectIdentity.

    :param sign_in_type:
    :type sign_in_type: str
    :param issuer:
    :type issuer: str
    :param issuer_assigned_id:
    :type issuer_assigned_id: str
    """

    _attribute_map = {
        'sign_in_type': {'key': 'signInType', 'type': 'str'},
        'issuer': {'key': 'issuer', 'type': 'str'},
        'issuer_assigned_id': {'key': 'issuerAssignedId', 'type': 'str'},
    }

    def __init__(self, sign_in_type=None, issuer=None, issuer_assigned_id=None):
        super(MicrosoftgraphobjectIdentity, self).__init__()
        self.sign_in_type = sign_in_type
        self.issuer = issuer
        self.issuer_assigned_id = issuer_assigned_id
