# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphsizeRange(Model):
    """sizeRange.

    :param minimum_size:
    :type minimum_size: int
    :param maximum_size:
    :type maximum_size: int
    """

    _validation = {
        'minimum_size': {'maximum': 2147483647, 'minimum': -2147483648},
        'maximum_size': {'maximum': 2147483647, 'minimum': -2147483648},
    }

    _attribute_map = {
        'minimum_size': {'key': 'minimumSize', 'type': 'int'},
        'maximum_size': {'key': 'maximumSize', 'type': 'int'},
    }

    def __init__(self, minimum_size=None, maximum_size=None):
        super(MicrosoftgraphsizeRange, self).__init__()
        self.minimum_size = minimum_size
        self.maximum_size = maximum_size