# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphWorkbookchartseriesformatallof1(Model):
    """workbookChartSeriesFormat.

    :param fill:
    :type fill: ~users.models.MicrosoftgraphworkbookChartFill
    :param line:
    :type line: ~users.models.MicrosoftgraphworkbookChartLineFormat
    """

    _attribute_map = {
        'fill': {'key': 'fill', 'type': 'MicrosoftgraphworkbookChartFill'},
        'line': {'key': 'line', 'type': 'MicrosoftgraphworkbookChartLineFormat'},
    }

    def __init__(self, fill=None, line=None):
        super(ComponentsschemasmicrosoftGraphWorkbookchartseriesformatallof1, self).__init__()
        self.fill = fill
        self.line = line
