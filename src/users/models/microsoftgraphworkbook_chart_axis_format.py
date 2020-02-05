# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphworkbookChartAxisFormat(Model):
    """MicrosoftgraphworkbookChartAxisFormat.

    :param id:
    :type id: str
    :param font:
    :type font: ~users.models.MicrosoftgraphworkbookChartFont
    :param line:
    :type line: ~users.models.MicrosoftgraphworkbookChartLineFormat
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'font': {'key': 'font', 'type': 'MicrosoftgraphworkbookChartFont'},
        'line': {'key': 'line', 'type': 'MicrosoftgraphworkbookChartLineFormat'},
    }

    def __init__(self, id=None, font=None, line=None):
        super(MicrosoftgraphworkbookChartAxisFormat, self).__init__()
        self.id = id
        self.font = font
        self.line = line