# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphlicenseProcessingState(Model):
    """licenseProcessingState.

    :param state:
    :type state: str
    """

    _attribute_map = {
        'state': {'key': 'state', 'type': 'str'},
    }

    def __init__(self, state=None):
        super(MicrosoftgraphlicenseProcessingState, self).__init__()
        self.state = state