# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphtimeOff(Model):
    """MicrosoftgraphtimeOff.

    :param id:
    :type id: str
    :param created_date_time:
    :type created_date_time: datetime
    :param last_modified_date_time:
    :type last_modified_date_time: datetime
    :param last_modified_by:
    :type last_modified_by: ~users.models.MicrosoftgraphidentitySet
    :param shared_time_off:
    :type shared_time_off: ~users.models.MicrosoftgraphtimeOffItem
    :param draft_time_off:
    :type draft_time_off: ~users.models.MicrosoftgraphtimeOffItem
    :param user_id:
    :type user_id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'last_modified_date_time': {'key': 'lastModifiedDateTime', 'type': 'iso-8601'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'MicrosoftgraphidentitySet'},
        'shared_time_off': {'key': 'sharedTimeOff', 'type': 'MicrosoftgraphtimeOffItem'},
        'draft_time_off': {'key': 'draftTimeOff', 'type': 'MicrosoftgraphtimeOffItem'},
        'user_id': {'key': 'userId', 'type': 'str'},
    }

    def __init__(self, id=None, created_date_time=None, last_modified_date_time=None, last_modified_by=None, shared_time_off=None, draft_time_off=None, user_id=None):
        super(MicrosoftgraphtimeOff, self).__init__()
        self.id = id
        self.created_date_time = created_date_time
        self.last_modified_date_time = last_modified_date_time
        self.last_modified_by = last_modified_by
        self.shared_time_off = shared_time_off
        self.draft_time_off = draft_time_off
        self.user_id = user_id
