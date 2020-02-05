# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphrecurrencePattern(Model):
    """recurrencePattern.

    :param type: Possible values include: 'daily', 'weekly',
     'absoluteMonthly', 'relativeMonthly', 'absoluteYearly', 'relativeYearly'
    :type type: str or ~users.models.enum
    :param interval:
    :type interval: int
    :param month:
    :type month: int
    :param day_of_month:
    :type day_of_month: int
    :param days_of_week:
    :type days_of_week: list[str]
    :param first_day_of_week: Possible values include: 'sunday', 'monday',
     'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'
    :type first_day_of_week: str or ~users.models.enum
    :param index: Possible values include: 'first', 'second', 'third',
     'fourth', 'last'
    :type index: str or ~users.models.enum
    """

    _validation = {
        'interval': {'maximum': 2147483647, 'minimum': -2147483648},
        'month': {'maximum': 2147483647, 'minimum': -2147483648},
        'day_of_month': {'maximum': 2147483647, 'minimum': -2147483648},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'interval': {'key': 'interval', 'type': 'int'},
        'month': {'key': 'month', 'type': 'int'},
        'day_of_month': {'key': 'dayOfMonth', 'type': 'int'},
        'days_of_week': {'key': 'daysOfWeek', 'type': '[str]'},
        'first_day_of_week': {'key': 'firstDayOfWeek', 'type': 'str'},
        'index': {'key': 'index', 'type': 'str'},
    }

    def __init__(self, type=None, interval=None, month=None, day_of_month=None, days_of_week=None, first_day_of_week=None, index=None):
        super(MicrosoftgraphrecurrencePattern, self).__init__()
        self.type = type
        self.interval = interval
        self.month = month
        self.day_of_month = day_of_month
        self.days_of_week = days_of_week
        self.first_day_of_week = first_day_of_week
        self.index = index