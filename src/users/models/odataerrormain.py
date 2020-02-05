# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Odataerrormain(Model):
    """Odataerrormain.

    :param code:
    :type code: str
    :param message:
    :type message: str
    :param target:
    :type target: str
    :param details:
    :type details: list[~users.models.Odataerrordetail]
    :param innererror: The structure of this object is service-specific
    :type innererror: object
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[Odataerrordetail]'},
        'innererror': {'key': 'innererror', 'type': 'object'},
    }

    def __init__(self, code, message, target=None, details=None, innererror=None):
        super(Odataerrormain, self).__init__()
        self.code = code
        self.message = message
        self.target = target
        self.details = details
        self.innererror = innererror