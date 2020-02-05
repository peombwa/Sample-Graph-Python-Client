# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphworkbookChartTitleFormat(Model):
    """MicrosoftgraphworkbookChartTitleFormat.

    :param id:
    :type id: str
    :param fill:
    :type fill: ~users.models.MicrosoftgraphworkbookChartFill
    :param font:
    :type font: ~users.models.MicrosoftgraphworkbookChartFont
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'fill': {'key': 'fill', 'type': 'MicrosoftgraphworkbookChartFill'},
        'font': {'key': 'font', 'type': 'MicrosoftgraphworkbookChartFont'},
    }

    def __init__(self, id=None, fill=None, font=None):
        super(MicrosoftgraphworkbookChartTitleFormat, self).__init__()
        self.id = id
        self.fill = fill
        self.font = font