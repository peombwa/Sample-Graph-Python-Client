# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphListallof1(Model):
    """list.

    :param display_name:
    :type display_name: str
    :param list:
    :type list: ~users.models.MicrosoftgraphlistInfo
    :param sharepoint_ids:
    :type sharepoint_ids: ~users.models.MicrosoftgraphsharepointIds
    :param system:
    :type system: object
    :param activities:
    :type activities: list[~users.models.MicrosoftgraphitemActivityOLD]
    :param columns:
    :type columns: list[~users.models.MicrosoftgraphcolumnDefinition]
    :param content_types:
    :type content_types: list[~users.models.MicrosoftgraphcontentType]
    :param drive:
    :type drive: ~users.models.Microsoftgraphdrive
    :param items:
    :type items: list[~users.models.MicrosoftgraphlistItem]
    :param subscriptions:
    :type subscriptions: list[~users.models.Microsoftgraphsubscription]
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'list': {'key': 'list', 'type': 'MicrosoftgraphlistInfo'},
        'sharepoint_ids': {'key': 'sharepointIds', 'type': 'MicrosoftgraphsharepointIds'},
        'system': {'key': 'system', 'type': 'object'},
        'activities': {'key': 'activities', 'type': '[MicrosoftgraphitemActivityOLD]'},
        'columns': {'key': 'columns', 'type': '[MicrosoftgraphcolumnDefinition]'},
        'content_types': {'key': 'contentTypes', 'type': '[MicrosoftgraphcontentType]'},
        'drive': {'key': 'drive', 'type': 'Microsoftgraphdrive'},
        'items': {'key': 'items', 'type': '[MicrosoftgraphlistItem]'},
        'subscriptions': {'key': 'subscriptions', 'type': '[Microsoftgraphsubscription]'},
    }

    def __init__(self, display_name=None, list=None, sharepoint_ids=None, system=None, activities=None, columns=None, content_types=None, drive=None, items=None, subscriptions=None):
        super(ComponentsschemasmicrosoftGraphListallof1, self).__init__()
        self.display_name = display_name
        self.list = list
        self.sharepoint_ids = sharepoint_ids
        self.system = system
        self.activities = activities
        self.columns = columns
        self.content_types = content_types
        self.drive = drive
        self.items = items
        self.subscriptions = subscriptions