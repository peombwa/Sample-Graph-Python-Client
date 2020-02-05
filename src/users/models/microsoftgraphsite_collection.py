# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphsiteCollection(Model):
    """siteCollection.

    :param data_location_code:
    :type data_location_code: str
    :param hostname:
    :type hostname: str
    :param root:
    :type root: object
    """

    _attribute_map = {
        'data_location_code': {'key': 'dataLocationCode', 'type': 'str'},
        'hostname': {'key': 'hostname', 'type': 'str'},
        'root': {'key': 'root', 'type': 'object'},
    }

    def __init__(self, data_location_code=None, hostname=None, root=None):
        super(MicrosoftgraphsiteCollection, self).__init__()
        self.data_location_code = data_location_code
        self.hostname = hostname
        self.root = root