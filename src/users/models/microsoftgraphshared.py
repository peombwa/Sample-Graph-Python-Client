# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Microsoftgraphshared(Model):
    """shared.

    :param owner:
    :type owner: ~users.models.MicrosoftgraphidentitySet
    :param scope:
    :type scope: str
    :param shared_by:
    :type shared_by: ~users.models.MicrosoftgraphidentitySet
    :param shared_date_time:
    :type shared_date_time: datetime
    """

    _attribute_map = {
        'owner': {'key': 'owner', 'type': 'MicrosoftgraphidentitySet'},
        'scope': {'key': 'scope', 'type': 'str'},
        'shared_by': {'key': 'sharedBy', 'type': 'MicrosoftgraphidentitySet'},
        'shared_date_time': {'key': 'sharedDateTime', 'type': 'iso-8601'},
    }

    def __init__(self, owner=None, scope=None, shared_by=None, shared_date_time=None):
        super(Microsoftgraphshared, self).__init__()
        self.owner = owner
        self.scope = scope
        self.shared_by = shared_by
        self.shared_date_time = shared_date_time