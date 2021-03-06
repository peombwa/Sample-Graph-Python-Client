# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphitemReference(Model):
    """itemReference.

    :param drive_id:
    :type drive_id: str
    :param drive_type:
    :type drive_type: str
    :param id:
    :type id: str
    :param name:
    :type name: str
    :param path:
    :type path: str
    :param share_id:
    :type share_id: str
    :param sharepoint_ids:
    :type sharepoint_ids: ~users.models.MicrosoftgraphsharepointIds
    :param site_id:
    :type site_id: str
    """

    _attribute_map = {
        'drive_id': {'key': 'driveId', 'type': 'str'},
        'drive_type': {'key': 'driveType', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'share_id': {'key': 'shareId', 'type': 'str'},
        'sharepoint_ids': {'key': 'sharepointIds', 'type': 'MicrosoftgraphsharepointIds'},
        'site_id': {'key': 'siteId', 'type': 'str'},
    }

    def __init__(self, drive_id=None, drive_type=None, id=None, name=None, path=None, share_id=None, sharepoint_ids=None, site_id=None):
        super(MicrosoftgraphitemReference, self).__init__()
        self.drive_id = drive_id
        self.drive_type = drive_type
        self.id = id
        self.name = name
        self.path = path
        self.share_id = share_id
        self.sharepoint_ids = sharepoint_ids
        self.site_id = site_id
