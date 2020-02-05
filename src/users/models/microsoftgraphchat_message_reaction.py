# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphchatMessageReaction(Model):
    """chatMessageReaction.

    :param reaction_type:
    :type reaction_type: str
    :param created_date_time:
    :type created_date_time: datetime
    :param user:
    :type user: ~users.models.MicrosoftgraphidentitySet
    """

    _attribute_map = {
        'reaction_type': {'key': 'reactionType', 'type': 'str'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'user': {'key': 'user', 'type': 'MicrosoftgraphidentitySet'},
    }

    def __init__(self, reaction_type=None, created_date_time=None, user=None):
        super(MicrosoftgraphchatMessageReaction, self).__init__()
        self.reaction_type = reaction_type
        self.created_date_time = created_date_time
        self.user = user
