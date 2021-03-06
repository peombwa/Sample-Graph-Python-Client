# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphitemActivity(Model):
    """MicrosoftgraphitemActivity.

    :param id:
    :type id: str
    :param access:
    :type access: object
    :param activity_date_time:
    :type activity_date_time: datetime
    :param actor:
    :type actor: ~users.models.MicrosoftgraphidentitySet
    :param drive_item:
    :type drive_item: ~users.models.MicrosoftgraphdriveItem
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'access': {'key': 'access', 'type': 'object'},
        'activity_date_time': {'key': 'activityDateTime', 'type': 'iso-8601'},
        'actor': {'key': 'actor', 'type': 'MicrosoftgraphidentitySet'},
        'drive_item': {'key': 'driveItem', 'type': 'MicrosoftgraphdriveItem'},
    }

    def __init__(self, id=None, access=None, activity_date_time=None, actor=None, drive_item=None):
        super(MicrosoftgraphitemActivity, self).__init__()
        self.id = id
        self.access = access
        self.activity_date_time = activity_date_time
        self.actor = actor
        self.drive_item = drive_item
