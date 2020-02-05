# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphTeamsasyncoperationallof1(Model):
    """teamsAsyncOperation.

    :param operation_type: Possible values include: 'invalid', 'cloneTeam',
     'archiveTeam', 'unarchiveTeam', 'createTeam', 'unknownFutureValue'
    :type operation_type: str or ~users.models.enum
    :param created_date_time:
    :type created_date_time: datetime
    :param status: Possible values include: 'invalid', 'notStarted',
     'inProgress', 'succeeded', 'failed', 'unknownFutureValue'
    :type status: str or ~users.models.enum
    :param last_action_date_time:
    :type last_action_date_time: datetime
    :param attempts_count:
    :type attempts_count: int
    :param target_resource_id:
    :type target_resource_id: str
    :param target_resource_location:
    :type target_resource_location: str
    :param error:
    :type error: ~users.models.MicrosoftgraphoperationError
    """

    _validation = {
        'attempts_count': {'maximum': 2147483647, 'minimum': -2147483648},
    }

    _attribute_map = {
        'operation_type': {'key': 'operationType', 'type': 'str'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'str'},
        'last_action_date_time': {'key': 'lastActionDateTime', 'type': 'iso-8601'},
        'attempts_count': {'key': 'attemptsCount', 'type': 'int'},
        'target_resource_id': {'key': 'targetResourceId', 'type': 'str'},
        'target_resource_location': {'key': 'targetResourceLocation', 'type': 'str'},
        'error': {'key': 'error', 'type': 'MicrosoftgraphoperationError'},
    }

    def __init__(self, operation_type=None, created_date_time=None, status=None, last_action_date_time=None, attempts_count=None, target_resource_id=None, target_resource_location=None, error=None):
        super(ComponentsschemasmicrosoftGraphTeamsasyncoperationallof1, self).__init__()
        self.operation_type = operation_type
        self.created_date_time = created_date_time
        self.status = status
        self.last_action_date_time = last_action_date_time
        self.attempts_count = attempts_count
        self.target_resource_id = target_resource_id
        self.target_resource_location = target_resource_location
        self.error = error