# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphserviceInformation(Model):
    """serviceInformation.

    :param name:
    :type name: str
    :param web_url:
    :type web_url: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'web_url': {'key': 'webUrl', 'type': 'str'},
    }

    def __init__(self, name=None, web_url=None):
        super(MicrosoftgraphserviceInformation, self).__init__()
        self.name = name
        self.web_url = web_url