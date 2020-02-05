# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphincompleteData(Model):
    """incompleteData.

    :param missing_data_before_date_time:
    :type missing_data_before_date_time: datetime
    :param was_throttled:
    :type was_throttled: bool
    """

    _attribute_map = {
        'missing_data_before_date_time': {'key': 'missingDataBeforeDateTime', 'type': 'iso-8601'},
        'was_throttled': {'key': 'wasThrottled', 'type': 'bool'},
    }

    def __init__(self, missing_data_before_date_time=None, was_throttled=None):
        super(MicrosoftgraphincompleteData, self).__init__()
        self.missing_data_before_date_time = missing_data_before_date_time
        self.was_throttled = was_throttled
