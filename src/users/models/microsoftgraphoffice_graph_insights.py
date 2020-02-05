# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphofficeGraphInsights(Model):
    """MicrosoftgraphofficeGraphInsights.

    :param id:
    :type id: str
    :param trending:
    :type trending: list[~users.models.Microsoftgraphtrending]
    :param shared:
    :type shared: list[~users.models.MicrosoftgraphsharedInsight]
    :param used:
    :type used: list[~users.models.MicrosoftgraphusedInsight]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'trending': {'key': 'trending', 'type': '[Microsoftgraphtrending]'},
        'shared': {'key': 'shared', 'type': '[MicrosoftgraphsharedInsight]'},
        'used': {'key': 'used', 'type': '[MicrosoftgraphusedInsight]'},
    }

    def __init__(self, id=None, trending=None, shared=None, used=None):
        super(MicrosoftgraphofficeGraphInsights, self).__init__()
        self.id = id
        self.trending = trending
        self.shared = shared
        self.used = used