# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphshareAction(Model):
    """shareAction.

    :param recipients:
    :type recipients: list[~users.models.MicrosoftgraphidentitySet]
    """

    _attribute_map = {
        'recipients': {'key': 'recipients', 'type': '[MicrosoftgraphidentitySet]'},
    }

    def __init__(self, recipients=None):
        super(MicrosoftgraphshareAction, self).__init__()
        self.recipients = recipients