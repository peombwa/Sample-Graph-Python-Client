# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphattendeeBase(Model):
    """MicrosoftgraphattendeeBase.

    :param email_address:
    :type email_address: ~users.models.MicrosoftgraphemailAddress
    :param type: Possible values include: 'required', 'optional', 'resource'
    :type type: str or ~users.models.enum
    """

    _attribute_map = {
        'email_address': {'key': 'emailAddress', 'type': 'MicrosoftgraphemailAddress'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, email_address=None, type=None):
        super(MicrosoftgraphattendeeBase, self).__init__()
        self.email_address = email_address
        self.type = type
