# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphoutlookCategory(Model):
    """MicrosoftgraphoutlookCategory.

    :param id:
    :type id: str
    :param display_name:
    :type display_name: str
    :param color: Possible values include: 'preset0', 'preset1', 'preset2',
     'preset3', 'preset4', 'preset5', 'preset6', 'preset7', 'preset8',
     'preset9', 'preset10', 'preset11', 'preset12', 'preset13', 'preset14',
     'preset15', 'preset16', 'preset17', 'preset18', 'preset19', 'preset20',
     'preset21', 'preset22', 'preset23', 'preset24', 'none'
    :type color: str or ~users.models.enum
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'color': {'key': 'color', 'type': 'str'},
    }

    def __init__(self, id=None, display_name=None, color=None):
        super(MicrosoftgraphoutlookCategory, self).__init__()
        self.id = id
        self.display_name = display_name
        self.color = color