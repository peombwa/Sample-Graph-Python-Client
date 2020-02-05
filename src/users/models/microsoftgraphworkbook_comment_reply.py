# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphworkbookCommentReply(Model):
    """MicrosoftgraphworkbookCommentReply.

    :param id:
    :type id: str
    :param content:
    :type content: str
    :param content_type:
    :type content_type: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'content': {'key': 'content', 'type': 'str'},
        'content_type': {'key': 'contentType', 'type': 'str'},
    }

    def __init__(self, id=None, content=None, content_type=None):
        super(MicrosoftgraphworkbookCommentReply, self).__init__()
        self.id = id
        self.content = content
        self.content_type = content_type
