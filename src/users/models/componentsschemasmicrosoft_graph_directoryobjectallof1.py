# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphDirectoryobjectallof1(Model):
    """directoryObject.

    Represents an Azure Active Directory object. The directoryObject type is
    the base type for many other directory entity types.

    :param deleted_date_time:
    :type deleted_date_time: datetime
    """

    _attribute_map = {
        'deleted_date_time': {'key': 'deletedDateTime', 'type': 'iso-8601'},
    }

    def __init__(self, deleted_date_time=None):
        super(ComponentsschemasmicrosoftGraphDirectoryobjectallof1, self).__init__()
        self.deleted_date_time = deleted_date_time
