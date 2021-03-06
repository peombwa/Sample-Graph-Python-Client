# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphitemActivityTimeSet(Model):
    """itemActivityTimeSet.

    :param last_recorded_date_time:
    :type last_recorded_date_time: datetime
    :param observed_date_time:
    :type observed_date_time: datetime
    :param recorded_date_time:
    :type recorded_date_time: datetime
    """

    _attribute_map = {
        'last_recorded_date_time': {'key': 'lastRecordedDateTime', 'type': 'iso-8601'},
        'observed_date_time': {'key': 'observedDateTime', 'type': 'iso-8601'},
        'recorded_date_time': {'key': 'recordedDateTime', 'type': 'iso-8601'},
    }

    def __init__(self, last_recorded_date_time=None, observed_date_time=None, recorded_date_time=None):
        super(MicrosoftgraphitemActivityTimeSet, self).__init__()
        self.last_recorded_date_time = last_recorded_date_time
        self.observed_date_time = observed_date_time
        self.recorded_date_time = recorded_date_time
