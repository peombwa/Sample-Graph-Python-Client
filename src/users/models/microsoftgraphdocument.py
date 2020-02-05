# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Microsoftgraphdocument(Model):
    """Microsoftgraphdocument.

    :param id:
    :type id: str
    :param comments:
    :type comments: list[~users.models.MicrosoftgraphdocumentComment]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'comments': {'key': 'comments', 'type': '[MicrosoftgraphdocumentComment]'},
    }

    def __init__(self, id=None, comments=None):
        super(Microsoftgraphdocument, self).__init__()
        self.id = id
        self.comments = comments