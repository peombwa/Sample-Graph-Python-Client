# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Microsoftgraphalbum(Model):
    """album.

    :param cover_image_item_id:
    :type cover_image_item_id: str
    """

    _attribute_map = {
        'cover_image_item_id': {'key': 'coverImageItemId', 'type': 'str'},
    }

    def __init__(self, cover_image_item_id=None):
        super(Microsoftgraphalbum, self).__init__()
        self.cover_image_item_id = cover_image_item_id
