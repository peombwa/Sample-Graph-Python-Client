# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphsitePage(Model):
    """MicrosoftgraphsitePage.

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
    :param title:
    :type title: str
    :param content_type:
    :type content_type: ~users.models.MicrosoftgraphcontentTypeInfo
    :param page_layout_type:
    :type page_layout_type: str
    :param web_parts:
    :type web_parts: list[~users.models.MicrosoftgraphwebPart]
    :param publishing_state:
    :type publishing_state: ~users.models.MicrosoftgraphpublicationFacet
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
        'title': {'key': 'title', 'type': 'str'},
        'content_type': {'key': 'contentType', 'type': 'MicrosoftgraphcontentTypeInfo'},
        'page_layout_type': {'key': 'pageLayoutType', 'type': 'str'},
        'web_parts': {'key': 'webParts', 'type': '[MicrosoftgraphwebPart]'},
        'publishing_state': {'key': 'publishingState', 'type': 'MicrosoftgraphpublicationFacet'},
    }

    def __init__(self, id=None, created_by=None, created_date_time=None, description=None, e_tag=None, last_modified_by=None, last_modified_date_time=None, name=None, parent_reference=None, web_url=None, created_by_user=None, last_modified_by_user=None, title=None, content_type=None, page_layout_type=None, web_parts=None, publishing_state=None):
        super(MicrosoftgraphsitePage, self).__init__()
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
        self.title = title
        self.content_type = content_type
        self.page_layout_type = page_layout_type
        self.web_parts = web_parts
        self.publishing_state = publishing_state
