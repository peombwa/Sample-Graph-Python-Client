# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphWorkbookchartpointformatallof1(Model):
    """workbookChartPointFormat.

    :param fill:
    :type fill: ~users.models.MicrosoftgraphworkbookChartFill
    """

    _attribute_map = {
        'fill': {'key': 'fill', 'type': 'MicrosoftgraphworkbookChartFill'},
    }

    def __init__(self, fill=None):
        super(ComponentsschemasmicrosoftGraphWorkbookchartpointformatallof1, self).__init__()
        self.fill = fill
