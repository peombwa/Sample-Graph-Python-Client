# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphWorkbookchartaxisallof1(Model):
    """workbookChartAxis.

    :param major_unit:
    :type major_unit: object
    :param maximum:
    :type maximum: object
    :param minimum:
    :type minimum: object
    :param minor_unit:
    :type minor_unit: object
    :param format:
    :type format: ~users.models.MicrosoftgraphworkbookChartAxisFormat
    :param major_gridlines:
    :type major_gridlines: ~users.models.MicrosoftgraphworkbookChartGridlines
    :param minor_gridlines:
    :type minor_gridlines: ~users.models.MicrosoftgraphworkbookChartGridlines
    :param title:
    :type title: ~users.models.MicrosoftgraphworkbookChartAxisTitle
    """

    _attribute_map = {
        'major_unit': {'key': 'majorUnit', 'type': 'object'},
        'maximum': {'key': 'maximum', 'type': 'object'},
        'minimum': {'key': 'minimum', 'type': 'object'},
        'minor_unit': {'key': 'minorUnit', 'type': 'object'},
        'format': {'key': 'format', 'type': 'MicrosoftgraphworkbookChartAxisFormat'},
        'major_gridlines': {'key': 'majorGridlines', 'type': 'MicrosoftgraphworkbookChartGridlines'},
        'minor_gridlines': {'key': 'minorGridlines', 'type': 'MicrosoftgraphworkbookChartGridlines'},
        'title': {'key': 'title', 'type': 'MicrosoftgraphworkbookChartAxisTitle'},
    }

    def __init__(self, major_unit=None, maximum=None, minimum=None, minor_unit=None, format=None, major_gridlines=None, minor_gridlines=None, title=None):
        super(ComponentsschemasmicrosoftGraphWorkbookchartaxisallof1, self).__init__()
        self.major_unit = major_unit
        self.maximum = maximum
        self.minimum = minimum
        self.minor_unit = minor_unit
        self.format = format
        self.major_gridlines = major_gridlines
        self.minor_gridlines = minor_gridlines
        self.title = title