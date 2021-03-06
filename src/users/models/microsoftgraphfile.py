# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Microsoftgraphfile(Model):
    """file.

    :param hashes:
    :type hashes: ~users.models.Microsoftgraphhashes
    :param mime_type:
    :type mime_type: str
    :param processing_metadata:
    :type processing_metadata: bool
    """

    _attribute_map = {
        'hashes': {'key': 'hashes', 'type': 'Microsoftgraphhashes'},
        'mime_type': {'key': 'mimeType', 'type': 'str'},
        'processing_metadata': {'key': 'processingMetadata', 'type': 'bool'},
    }

    def __init__(self, hashes=None, mime_type=None, processing_metadata=None):
        super(Microsoftgraphfile, self).__init__()
        self.hashes = hashes
        self.mime_type = mime_type
        self.processing_metadata = processing_metadata
