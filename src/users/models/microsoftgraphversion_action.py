# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphversionAction(Model):
    """versionAction.

    :param new_version:
    :type new_version: str
    """

    _attribute_map = {
        'new_version': {'key': 'newVersion', 'type': 'str'},
    }

    def __init__(self, new_version=None):
        super(MicrosoftgraphversionAction, self).__init__()
        self.new_version = new_version
