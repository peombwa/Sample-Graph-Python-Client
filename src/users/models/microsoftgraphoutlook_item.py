# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphoutlookItem(Model):
    """MicrosoftgraphoutlookItem.

    :param id:
    :type id: str
    :param created_date_time:
    :type created_date_time: datetime
    :param last_modified_date_time:
    :type last_modified_date_time: datetime
    :param change_key:
    :type change_key: str
    :param categories:
    :type categories: list[str]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'last_modified_date_time': {'key': 'lastModifiedDateTime', 'type': 'iso-8601'},
        'change_key': {'key': 'changeKey', 'type': 'str'},
        'categories': {'key': 'categories', 'type': '[str]'},
    }

    def __init__(self, id=None, created_date_time=None, last_modified_date_time=None, change_key=None, categories=None):
        super(MicrosoftgraphoutlookItem, self).__init__()
        self.id = id
        self.created_date_time = created_date_time
        self.last_modified_date_time = last_modified_date_time
        self.change_key = change_key
        self.categories = categories
