# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphexternalLink(Model):
    """externalLink.

    :param href:
    :type href: str
    """

    _attribute_map = {
        'href': {'key': 'href', 'type': 'str'},
    }

    def __init__(self, href=None):
        super(MicrosoftgraphexternalLink, self).__init__()
        self.href = href
