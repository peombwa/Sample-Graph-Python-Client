# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphrankedEmailAddress(Model):
    """rankedEmailAddress.

    :param address:
    :type address: str
    :param rank:
    :type rank: float
    """

    _attribute_map = {
        'address': {'key': 'address', 'type': 'str'},
        'rank': {'key': 'rank', 'type': 'float'},
    }

    def __init__(self, address=None, rank=None):
        super(MicrosoftgraphrankedEmailAddress, self).__init__()
        self.address = address
        self.rank = rank
