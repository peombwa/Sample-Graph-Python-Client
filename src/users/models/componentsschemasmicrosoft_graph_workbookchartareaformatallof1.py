# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphWorkbookchartareaformatallof1(Model):
    """workbookChartAreaFormat.

    :param fill:
    :type fill: ~users.models.MicrosoftgraphworkbookChartFill
    :param font:
    :type font: ~users.models.MicrosoftgraphworkbookChartFont
    """

    _attribute_map = {
        'fill': {'key': 'fill', 'type': 'MicrosoftgraphworkbookChartFill'},
        'font': {'key': 'font', 'type': 'MicrosoftgraphworkbookChartFont'},
    }

    def __init__(self, fill=None, font=None):
        super(ComponentsschemasmicrosoftGraphWorkbookchartareaformatallof1, self).__init__()
        self.fill = fill
        self.font = font
