# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphworkbookPivotTable(Model):
    """MicrosoftgraphworkbookPivotTable.

    :param id:
    :type id: str
    :param name:
    :type name: str
    :param worksheet:
    :type worksheet: ~users.models.MicrosoftgraphworkbookWorksheet
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'worksheet': {'key': 'worksheet', 'type': 'MicrosoftgraphworkbookWorksheet'},
    }

    def __init__(self, id=None, name=None, worksheet=None):
        super(MicrosoftgraphworkbookPivotTable, self).__init__()
        self.id = id
        self.name = name
        self.worksheet = worksheet
