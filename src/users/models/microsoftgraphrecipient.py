# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Microsoftgraphrecipient(Model):
    """recipient.

    :param email_address:
    :type email_address: ~users.models.MicrosoftgraphemailAddress
    """

    _attribute_map = {
        'email_address': {'key': 'emailAddress', 'type': 'MicrosoftgraphemailAddress'},
    }

    def __init__(self, email_address=None):
        super(Microsoftgraphrecipient, self).__init__()
        self.email_address = email_address
