# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphWorkbookchartlineformatallof1(Model):
    """workbookChartLineFormat.

    :param color:
    :type color: str
    """

    _attribute_map = {
        'color': {'key': 'color', 'type': 'str'},
    }

    def __init__(self, color=None):
        super(ComponentsschemasmicrosoftGraphWorkbookchartlineformatallof1, self).__init__()
        self.color = color
