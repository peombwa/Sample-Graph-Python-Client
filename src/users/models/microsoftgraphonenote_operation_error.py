# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphonenoteOperationError(Model):
    """onenoteOperationError.

    :param code:
    :type code: str
    :param message:
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, code=None, message=None):
        super(MicrosoftgraphonenoteOperationError, self).__init__()
        self.code = code
        self.message = message
