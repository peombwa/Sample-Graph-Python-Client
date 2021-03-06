# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphonenoteOperation(Model):
    """MicrosoftgraphonenoteOperation.

    :param id:
    :type id: str
    :param status: Possible values include: 'NotStarted', 'Running',
     'Completed', 'Failed'
    :type status: str or ~users.models.enum
    :param created_date_time:
    :type created_date_time: datetime
    :param last_action_date_time:
    :type last_action_date_time: datetime
    :param resource_location:
    :type resource_location: str
    :param resource_id:
    :type resource_id: str
    :param error:
    :type error: ~users.models.MicrosoftgraphonenoteOperationError
    :param percent_complete:
    :type percent_complete: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'last_action_date_time': {'key': 'lastActionDateTime', 'type': 'iso-8601'},
        'resource_location': {'key': 'resourceLocation', 'type': 'str'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'error': {'key': 'error', 'type': 'MicrosoftgraphonenoteOperationError'},
        'percent_complete': {'key': 'percentComplete', 'type': 'str'},
    }

    def __init__(self, id=None, status=None, created_date_time=None, last_action_date_time=None, resource_location=None, resource_id=None, error=None, percent_complete=None):
        super(MicrosoftgraphonenoteOperation, self).__init__()
        self.id = id
        self.status = status
        self.created_date_time = created_date_time
        self.last_action_date_time = last_action_date_time
        self.resource_location = resource_location
        self.resource_id = resource_id
        self.error = error
        self.percent_complete = percent_complete
