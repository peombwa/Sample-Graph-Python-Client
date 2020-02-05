# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphTimeoffrequestallof1(Model):
    """timeOffRequest.

    :param start_date_time:
    :type start_date_time: datetime
    :param end_date_time:
    :type end_date_time: datetime
    :param time_off_reason_id:
    :type time_off_reason_id: str
    """

    _attribute_map = {
        'start_date_time': {'key': 'startDateTime', 'type': 'iso-8601'},
        'end_date_time': {'key': 'endDateTime', 'type': 'iso-8601'},
        'time_off_reason_id': {'key': 'timeOffReasonId', 'type': 'str'},
    }

    def __init__(self, start_date_time=None, end_date_time=None, time_off_reason_id=None):
        super(ComponentsschemasmicrosoftGraphTimeoffrequestallof1, self).__init__()
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.time_off_reason_id = time_off_reason_id