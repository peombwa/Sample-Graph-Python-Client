# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphworkbookChartFont(Model):
    """MicrosoftgraphworkbookChartFont.

    :param id:
    :type id: str
    :param bold:
    :type bold: bool
    :param color:
    :type color: str
    :param italic:
    :type italic: bool
    :param name:
    :type name: str
    :param size:
    :type size: float
    :param underline:
    :type underline: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'bold': {'key': 'bold', 'type': 'bool'},
        'color': {'key': 'color', 'type': 'str'},
        'italic': {'key': 'italic', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'size': {'key': 'size', 'type': 'float'},
        'underline': {'key': 'underline', 'type': 'str'},
    }

    def __init__(self, id=None, bold=None, color=None, italic=None, name=None, size=None, underline=None):
        super(MicrosoftgraphworkbookChartFont, self).__init__()
        self.id = id
        self.bold = bold
        self.color = color
        self.italic = italic
        self.name = name
        self.size = size
        self.underline = underline
