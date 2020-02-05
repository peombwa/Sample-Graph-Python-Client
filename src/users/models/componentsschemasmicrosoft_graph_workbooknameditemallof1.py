# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphWorkbooknameditemallof1(Model):
    """workbookNamedItem.

    :param comment:
    :type comment: str
    :param name:
    :type name: str
    :param scope:
    :type scope: str
    :param type:
    :type type: str
    :param value:
    :type value: object
    :param visible:
    :type visible: bool
    :param worksheet:
    :type worksheet: ~users.models.MicrosoftgraphworkbookWorksheet
    """

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'scope': {'key': 'scope', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'},
        'visible': {'key': 'visible', 'type': 'bool'},
        'worksheet': {'key': 'worksheet', 'type': 'MicrosoftgraphworkbookWorksheet'},
    }

    def __init__(self, comment=None, name=None, scope=None, type=None, value=None, visible=None, worksheet=None):
        super(ComponentsschemasmicrosoftGraphWorkbooknameditemallof1, self).__init__()
        self.comment = comment
        self.name = name
        self.scope = scope
        self.type = type
        self.value = value
        self.visible = visible
        self.worksheet = worksheet
