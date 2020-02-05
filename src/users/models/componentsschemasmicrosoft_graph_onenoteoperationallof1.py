# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphOnenoteoperationallof1(Model):
    """onenoteOperation.

    :param resource_location:
    :type resource_location: str
    :param resource_id:
    :type resource_id: str
    :param error:
    :type error: ~users.models.MicrosoftgraphonenoteOperationError
    :param percent_complete:
    :type percent_complete: str
    """

    _attribute_map = {
        'resource_location': {'key': 'resourceLocation', 'type': 'str'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'error': {'key': 'error', 'type': 'MicrosoftgraphonenoteOperationError'},
        'percent_complete': {'key': 'percentComplete', 'type': 'str'},
    }

    def __init__(self, resource_location=None, resource_id=None, error=None, percent_complete=None):
        super(ComponentsschemasmicrosoftGraphOnenoteoperationallof1, self).__init__()
        self.resource_location = resource_location
        self.resource_id = resource_id
        self.error = error
        self.percent_complete = percent_complete
