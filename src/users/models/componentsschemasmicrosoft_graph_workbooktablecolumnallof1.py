# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphWorkbooktablecolumnallof1(Model):
    """workbookTableColumn.

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
        'index': {'key': 'index', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'values': {'key': 'values', 'type': 'object'},
        'filter': {'key': 'filter', 'type': 'MicrosoftgraphworkbookFilter'},
    }

    def __init__(self, index=None, name=None, values=None, filter=None):
        super(ComponentsschemasmicrosoftGraphWorkbooktablecolumnallof1, self).__init__()
        self.index = index
        self.name = name
        self.values = values
        self.filter = filter
