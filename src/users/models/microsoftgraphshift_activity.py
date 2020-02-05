# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphshiftActivity(Model):
    """shiftActivity.

    :param is_paid:
    :type is_paid: bool
    :param start_date_time:
    :type start_date_time: datetime
    :param end_date_time:
    :type end_date_time: datetime
    :param code:
    :type code: str
    :param display_name:
    :type display_name: str
    :param theme: Possible values include: 'white', 'blue', 'green', 'purple',
     'pink', 'yellow', 'gray', 'darkBlue', 'darkGreen', 'darkPurple',
     'darkPink', 'darkYellow', 'unknownFutureValue'
    :type theme: str or ~users.models.enum
    """

    _attribute_map = {
        'is_paid': {'key': 'isPaid', 'type': 'bool'},
        'start_date_time': {'key': 'startDateTime', 'type': 'iso-8601'},
        'end_date_time': {'key': 'endDateTime', 'type': 'iso-8601'},
        'code': {'key': 'code', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'theme': {'key': 'theme', 'type': 'str'},
    }

    def __init__(self, is_paid=None, start_date_time=None, end_date_time=None, code=None, display_name=None, theme=None):
        super(MicrosoftgraphshiftActivity, self).__init__()
        self.is_paid = is_paid
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.code = code
        self.display_name = display_name
        self.theme = theme
