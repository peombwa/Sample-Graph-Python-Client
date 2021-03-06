# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphlistItem(Model):
    """MicrosoftgraphlistItem.

    :param id:
    :type id: str
    :param created_by:
    :type created_by: ~users.models.MicrosoftgraphidentitySet
    :param created_date_time:
    :type created_date_time: datetime
    :param description:
    :type description: str
    :param e_tag:
    :type e_tag: str
    :param last_modified_by:
    :type last_modified_by: ~users.models.MicrosoftgraphidentitySet
    :param last_modified_date_time:
    :type last_modified_date_time: datetime
    :param name:
    :type name: str
    :param parent_reference:
    :type parent_reference: ~users.models.MicrosoftgraphitemReference
    :param web_url:
    :type web_url: str
    :param created_by_user:
    :type created_by_user: ~users.models.Microsoftgraphuser
    :param last_modified_by_user:
    :type last_modified_by_user: ~users.models.Microsoftgraphuser
    :param content_type:
    :type content_type: ~users.models.MicrosoftgraphcontentTypeInfo
    :param sharepoint_ids:
    :type sharepoint_ids: ~users.models.MicrosoftgraphsharepointIds
    :param activities:
    :type activities: list[~users.models.MicrosoftgraphitemActivityOLD]
    :param analytics:
    :type analytics: ~users.models.MicrosoftgraphitemAnalytics
    :param drive_item:
    :type drive_item: ~users.models.MicrosoftgraphdriveItem
    :param fields:
    :type fields: ~users.models.MicrosoftgraphfieldValueSet
    :param versions:
    :type versions: list[~users.models.MicrosoftgraphlistItemVersion]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'created_by': {'key': 'createdBy', 'type': 'MicrosoftgraphidentitySet'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'e_tag': {'key': 'eTag', 'type': 'str'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'MicrosoftgraphidentitySet'},
        'last_modified_date_time': {'key': 'lastModifiedDateTime', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'parent_reference': {'key': 'parentReference', 'type': 'MicrosoftgraphitemReference'},
        'web_url': {'key': 'webUrl', 'type': 'str'},
        'created_by_user': {'key': 'createdByUser', 'type': 'Microsoftgraphuser'},
        'last_modified_by_user': {'key': 'lastModifiedByUser', 'type': 'Microsoftgraphuser'},
        'content_type': {'key': 'contentType', 'type': 'MicrosoftgraphcontentTypeInfo'},
        'sharepoint_ids': {'key': 'sharepointIds', 'type': 'MicrosoftgraphsharepointIds'},
        'activities': {'key': 'activities', 'type': '[MicrosoftgraphitemActivityOLD]'},
        'analytics': {'key': 'analytics', 'type': 'MicrosoftgraphitemAnalytics'},
        'drive_item': {'key': 'driveItem', 'type': 'MicrosoftgraphdriveItem'},
        'fields': {'key': 'fields', 'type': 'MicrosoftgraphfieldValueSet'},
        'versions': {'key': 'versions', 'type': '[MicrosoftgraphlistItemVersion]'},
    }

    def __init__(self, id=None, created_by=None, created_date_time=None, description=None, e_tag=None, last_modified_by=None, last_modified_date_time=None, name=None, parent_reference=None, web_url=None, created_by_user=None, last_modified_by_user=None, content_type=None, sharepoint_ids=None, activities=None, analytics=None, drive_item=None, fields=None, versions=None):
        super(MicrosoftgraphlistItem, self).__init__()
        self.id = id
        self.created_by = created_by
        self.created_date_time = created_date_time
        self.description = description
        self.e_tag = e_tag
        self.last_modified_by = last_modified_by
        self.last_modified_date_time = last_modified_date_time
        self.name = name
        self.parent_reference = parent_reference
        self.web_url = web_url
        self.created_by_user = created_by_user
        self.last_modified_by_user = last_modified_by_user
        self.content_type = content_type
        self.sharepoint_ids = sharepoint_ids
        self.activities = activities
        self.analytics = analytics
        self.drive_item = drive_item
        self.fields = fields
        self.versions = versions
