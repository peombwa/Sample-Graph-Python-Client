# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphlocaleInfo(Model):
    """localeInfo.

    :param locale:
    :type locale: str
    :param display_name:
    :type display_name: str
    """

    _attribute_map = {
        'locale': {'key': 'locale', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
    }

    def __init__(self, locale=None, display_name=None):
        super(MicrosoftgraphlocaleInfo, self).__init__()
        self.locale = locale
        self.display_name = display_name
