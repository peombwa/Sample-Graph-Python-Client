# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphsharingInvitation(Model):
    """sharingInvitation.

    :param email:
    :type email: str
    :param invited_by:
    :type invited_by: ~users.models.MicrosoftgraphidentitySet
    :param redeemed_by:
    :type redeemed_by: str
    :param sign_in_required:
    :type sign_in_required: bool
    """

    _attribute_map = {
        'email': {'key': 'email', 'type': 'str'},
        'invited_by': {'key': 'invitedBy', 'type': 'MicrosoftgraphidentitySet'},
        'redeemed_by': {'key': 'redeemedBy', 'type': 'str'},
        'sign_in_required': {'key': 'signInRequired', 'type': 'bool'},
    }

    def __init__(self, email=None, invited_by=None, redeemed_by=None, sign_in_required=None):
        super(MicrosoftgraphsharingInvitation, self).__init__()
        self.email = email
        self.invited_by = invited_by
        self.redeemed_by = redeemed_by
        self.sign_in_required = sign_in_required
