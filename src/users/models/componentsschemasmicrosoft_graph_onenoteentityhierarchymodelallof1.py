# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphOnenoteentityhierarchymodelallof1(Model):
    """onenoteEntityHierarchyModel.

    :param display_name:
    :type display_name: str
    :param created_by:
    :type created_by: ~users.models.MicrosoftgraphidentitySet
    :param last_modified_by:
    :type last_modified_by: ~users.models.MicrosoftgraphidentitySet
    :param last_modified_date_time:
    :type last_modified_date_time: datetime
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'created_by': {'key': 'createdBy', 'type': 'MicrosoftgraphidentitySet'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'MicrosoftgraphidentitySet'},
        'last_modified_date_time': {'key': 'lastModifiedDateTime', 'type': 'iso-8601'},
    }

    def __init__(self, display_name=None, created_by=None, last_modified_by=None, last_modified_date_time=None):
        super(ComponentsschemasmicrosoftGraphOnenoteentityhierarchymodelallof1, self).__init__()
        self.display_name = display_name
        self.created_by = created_by
        self.last_modified_by = last_modified_by
        self.last_modified_date_time = last_modified_date_time
