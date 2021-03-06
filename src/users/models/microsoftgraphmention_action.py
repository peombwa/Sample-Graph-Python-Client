# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphmentionAction(Model):
    """mentionAction.

    :param mentionees:
    :type mentionees: list[~users.models.MicrosoftgraphidentitySet]
    """

    _attribute_map = {
        'mentionees': {'key': 'mentionees', 'type': '[MicrosoftgraphidentitySet]'},
    }

    def __init__(self, mentionees=None):
        super(MicrosoftgraphmentionAction, self).__init__()
        self.mentionees = mentionees
