# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphItemactivitystatallof1(Model):
    """itemActivityStat.

    :param start_date_time:
    :type start_date_time: datetime
    :param end_date_time:
    :type end_date_time: datetime
    :param access:
    :type access: ~users.models.MicrosoftgraphitemActionStat
    :param create:
    :type create: ~users.models.MicrosoftgraphitemActionStat
    :param delete:
    :type delete: ~users.models.MicrosoftgraphitemActionStat
    :param edit:
    :type edit: ~users.models.MicrosoftgraphitemActionStat
    :param move:
    :type move: ~users.models.MicrosoftgraphitemActionStat
    :param is_trending:
    :type is_trending: bool
    :param incomplete_data:
    :type incomplete_data: ~users.models.MicrosoftgraphincompleteData
    :param activities:
    :type activities: list[~users.models.MicrosoftgraphitemActivity]
    """

    _attribute_map = {
        'start_date_time': {'key': 'startDateTime', 'type': 'iso-8601'},
        'end_date_time': {'key': 'endDateTime', 'type': 'iso-8601'},
        'access': {'key': 'access', 'type': 'MicrosoftgraphitemActionStat'},
        'create': {'key': 'create', 'type': 'MicrosoftgraphitemActionStat'},
        'delete': {'key': 'delete', 'type': 'MicrosoftgraphitemActionStat'},
        'edit': {'key': 'edit', 'type': 'MicrosoftgraphitemActionStat'},
        'move': {'key': 'move', 'type': 'MicrosoftgraphitemActionStat'},
        'is_trending': {'key': 'isTrending', 'type': 'bool'},
        'incomplete_data': {'key': 'incompleteData', 'type': 'MicrosoftgraphincompleteData'},
        'activities': {'key': 'activities', 'type': '[MicrosoftgraphitemActivity]'},
    }

    def __init__(self, start_date_time=None, end_date_time=None, access=None, create=None, delete=None, edit=None, move=None, is_trending=None, incomplete_data=None, activities=None):
        super(ComponentsschemasmicrosoftGraphItemactivitystatallof1, self).__init__()
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.access = access
        self.create = create
        self.delete = delete
        self.edit = edit
        self.move = move
        self.is_trending = is_trending
        self.incomplete_data = incomplete_data
        self.activities = activities