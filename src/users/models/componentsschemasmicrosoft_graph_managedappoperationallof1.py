# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphManagedappoperationallof1(Model):
    """managedAppOperation.

    Represents an operation applied against an app registration.

    :param display_name: The operation name.
    :type display_name: str
    :param last_modified_date_time: The last time the app operation was
     modified.
    :type last_modified_date_time: datetime
    :param state: The current state of the operation
    :type state: str
    :param version: Version of the entity.
    :type version: str
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'last_modified_date_time': {'key': 'lastModifiedDateTime', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, display_name=None, last_modified_date_time=None, state=None, version=None):
        super(ComponentsschemasmicrosoftGraphManagedappoperationallof1, self).__init__()
        self.display_name = display_name
        self.last_modified_date_time = last_modified_date_time
        self.state = state
        self.version = version
