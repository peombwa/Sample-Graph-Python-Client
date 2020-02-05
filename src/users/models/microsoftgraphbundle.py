# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Microsoftgraphbundle(Model):
    """bundle.

    :param child_count:
    :type child_count: int
    :param album:
    :type album: ~users.models.Microsoftgraphalbum
    """

    _validation = {
        'child_count': {'maximum': 2147483647, 'minimum': -2147483648},
    }

    _attribute_map = {
        'child_count': {'key': 'childCount', 'type': 'int'},
        'album': {'key': 'album', 'type': 'Microsoftgraphalbum'},
    }

    def __init__(self, child_count=None, album=None):
        super(Microsoftgraphbundle, self).__init__()
        self.child_count = child_count
        self.album = album