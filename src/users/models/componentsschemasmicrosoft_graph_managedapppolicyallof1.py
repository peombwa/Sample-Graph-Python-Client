# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphManagedapppolicyallof1(Model):
    """managedAppPolicy.

    The ManagedAppPolicy resource represents a base type for platform specific
    policies.

    :param display_name: Policy display name.
    :type display_name: str
    :param description: The policy's description.
    :type description: str
    :param created_date_time: The date and time the policy was created.
    :type created_date_time: datetime
    :param last_modified_date_time: Last time the policy was modified.
    :type last_modified_date_time: datetime
    :param role_scope_tag_ids: List of Scope Tags for this Entity instance.
    :type role_scope_tag_ids: list[str]
    :param version: Version of the entity.
    :type version: str
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'last_modified_date_time': {'key': 'lastModifiedDateTime', 'type': 'iso-8601'},
        'role_scope_tag_ids': {'key': 'roleScopeTagIds', 'type': '[str]'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, display_name=None, description=None, created_date_time=None, last_modified_date_time=None, role_scope_tag_ids=None, version=None):
        super(ComponentsschemasmicrosoftGraphManagedapppolicyallof1, self).__init__()
        self.display_name = display_name
        self.description = description
        self.created_date_time = created_date_time
        self.last_modified_date_time = last_modified_date_time
        self.role_scope_tag_ids = role_scope_tag_ids
        self.version = version