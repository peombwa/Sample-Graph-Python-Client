# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphApproleassignmentallof1(Model):
    """appRoleAssignment.

    :param app_role_id:
    :type app_role_id: str
    :param creation_timestamp:
    :type creation_timestamp: datetime
    :param principal_display_name:
    :type principal_display_name: str
    :param principal_id:
    :type principal_id: str
    :param principal_type:
    :type principal_type: str
    :param resource_display_name:
    :type resource_display_name: str
    :param resource_id:
    :type resource_id: str
    """

    _attribute_map = {
        'app_role_id': {'key': 'appRoleId', 'type': 'str'},
        'creation_timestamp': {'key': 'creationTimestamp', 'type': 'iso-8601'},
        'principal_display_name': {'key': 'principalDisplayName', 'type': 'str'},
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'principal_type': {'key': 'principalType', 'type': 'str'},
        'resource_display_name': {'key': 'resourceDisplayName', 'type': 'str'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
    }

    def __init__(self, app_role_id=None, creation_timestamp=None, principal_display_name=None, principal_id=None, principal_type=None, resource_display_name=None, resource_id=None):
        super(ComponentsschemasmicrosoftGraphApproleassignmentallof1, self).__init__()
        self.app_role_id = app_role_id
        self.creation_timestamp = creation_timestamp
        self.principal_display_name = principal_display_name
        self.principal_id = principal_id
        self.principal_type = principal_type
        self.resource_display_name = resource_display_name
        self.resource_id = resource_id
