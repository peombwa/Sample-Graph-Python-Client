# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphloggedOnUser(Model):
    """loggedOnUser.

    :param user_id: User id
    :type user_id: str
    :param last_log_on_date_time: Date time when user logs on
    :type last_log_on_date_time: datetime
    """

    _attribute_map = {
        'user_id': {'key': 'userId', 'type': 'str'},
        'last_log_on_date_time': {'key': 'lastLogOnDateTime', 'type': 'iso-8601'},
    }

    def __init__(self, user_id=None, last_log_on_date_time=None):
        super(MicrosoftgraphloggedOnUser, self).__init__()
        self.user_id = user_id
        self.last_log_on_date_time = last_log_on_date_time