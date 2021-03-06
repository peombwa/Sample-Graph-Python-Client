# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphcalendarPermission(Model):
    """MicrosoftgraphcalendarPermission.

    :param id:
    :type id: str
    :param email_address:
    :type email_address: ~users.models.MicrosoftgraphemailAddress
    :param is_removable:
    :type is_removable: bool
    :param is_inside_organization:
    :type is_inside_organization: bool
    :param role: Possible values include: 'none', 'freeBusyRead',
     'limitedRead', 'read', 'write', 'delegateWithoutPrivateEventAccess',
     'delegateWithPrivateEventAccess', 'custom'
    :type role: str or ~users.models.enum
    :param allowed_roles:
    :type allowed_roles: list[str]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'email_address': {'key': 'emailAddress', 'type': 'MicrosoftgraphemailAddress'},
        'is_removable': {'key': 'isRemovable', 'type': 'bool'},
        'is_inside_organization': {'key': 'isInsideOrganization', 'type': 'bool'},
        'role': {'key': 'role', 'type': 'str'},
        'allowed_roles': {'key': 'allowedRoles', 'type': '[str]'},
    }

    def __init__(self, id=None, email_address=None, is_removable=None, is_inside_organization=None, role=None, allowed_roles=None):
        super(MicrosoftgraphcalendarPermission, self).__init__()
        self.id = id
        self.email_address = email_address
        self.is_removable = is_removable
        self.is_inside_organization = is_inside_organization
        self.role = role
        self.allowed_roles = allowed_roles
