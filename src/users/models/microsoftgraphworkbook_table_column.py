# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphworkbookTableColumn(Model):
    """MicrosoftgraphworkbookTableColumn.

    :param id:
    :type id: str
    :param index:
    :type index: int
    :param name:
    :type name: str
    :param values:
    :type values: object
    :param filter:
    :type filter: ~users.models.MicrosoftgraphworkbookFilter
    """

    _validation = {
        'index': {'maximum': 2147483647, 'minimum': -2147483648},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'index': {'key': 'index', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'values': {'key': 'values', 'type': 'object'},
        'filter': {'key': 'filter', 'type': 'MicrosoftgraphworkbookFilter'},
    }

    def __init__(self, id=None, index=None, name=None, values=None, filter=None):
        super(MicrosoftgraphworkbookTableColumn, self).__init__()
        self.id = id
        self.index = index
        self.name = name
        self.values = values
        self.filter = filter
