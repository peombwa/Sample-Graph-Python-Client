# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphworkbookChartGridlines(Model):
    """MicrosoftgraphworkbookChartGridlines.

    :param id:
    :type id: str
    :param visible:
    :type visible: bool
    :param format:
    :type format: ~users.models.MicrosoftgraphworkbookChartGridlinesFormat
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'visible': {'key': 'visible', 'type': 'bool'},
        'format': {'key': 'format', 'type': 'MicrosoftgraphworkbookChartGridlinesFormat'},
    }

    def __init__(self, id=None, visible=None, format=None):
        super(MicrosoftgraphworkbookChartGridlines, self).__init__()
        self.id = id
        self.visible = visible
        self.format = format
