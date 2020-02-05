# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphsectionGroup(Model):
    """MicrosoftgraphsectionGroup.

    :param id:
    :type id: str
    :param self:
    :type self: str
    :param created_date_time:
    :type created_date_time: datetime
    :param display_name:
    :type display_name: str
    :param created_by:
    :type created_by: ~users.models.MicrosoftgraphidentitySet
    :param last_modified_by:
    :type last_modified_by: ~users.models.MicrosoftgraphidentitySet
    :param last_modified_date_time:
    :type last_modified_date_time: datetime
    :param sections_url:
    :type sections_url: str
    :param section_groups_url:
    :type section_groups_url: str
    :param parent_notebook:
    :type parent_notebook: ~users.models.Microsoftgraphnotebook
    :param parent_section_group:
    :type parent_section_group: ~users.models.MicrosoftgraphsectionGroup
    :param sections:
    :type sections: list[~users.models.MicrosoftgraphonenoteSection]
    :param section_groups:
    :type section_groups: list[~users.models.MicrosoftgraphsectionGroup]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'self': {'key': 'self', 'type': 'str'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'created_by': {'key': 'createdBy', 'type': 'MicrosoftgraphidentitySet'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'MicrosoftgraphidentitySet'},
        'last_modified_date_time': {'key': 'lastModifiedDateTime', 'type': 'iso-8601'},
        'sections_url': {'key': 'sectionsUrl', 'type': 'str'},
        'section_groups_url': {'key': 'sectionGroupsUrl', 'type': 'str'},
        'parent_notebook': {'key': 'parentNotebook', 'type': 'Microsoftgraphnotebook'},
        'parent_section_group': {'key': 'parentSectionGroup', 'type': 'MicrosoftgraphsectionGroup'},
        'sections': {'key': 'sections', 'type': '[MicrosoftgraphonenoteSection]'},
        'section_groups': {'key': 'sectionGroups', 'type': '[MicrosoftgraphsectionGroup]'},
    }

    def __init__(self, id=None, self=None, created_date_time=None, display_name=None, created_by=None, last_modified_by=None, last_modified_date_time=None, sections_url=None, section_groups_url=None, parent_notebook=None, parent_section_group=None, sections=None, section_groups=None):
        super(MicrosoftgraphsectionGroup, self).__init__()
        self.id = id
        self.self = self
        self.created_date_time = created_date_time
        self.display_name = display_name
        self.created_by = created_by
        self.last_modified_by = last_modified_by
        self.last_modified_date_time = last_modified_date_time
        self.sections_url = sections_url
        self.section_groups_url = section_groups_url
        self.parent_notebook = parent_notebook
        self.parent_section_group = parent_section_group
        self.sections = sections
        self.section_groups = section_groups
