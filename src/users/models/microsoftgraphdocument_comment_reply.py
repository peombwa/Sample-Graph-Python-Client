# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphdocumentCommentReply(Model):
    """MicrosoftgraphdocumentCommentReply.

    :param id:
    :type id: str
    :param content:
    :type content: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'content': {'key': 'content', 'type': 'str'},
    }

    def __init__(self, id=None, content=None):
        super(MicrosoftgraphdocumentCommentReply, self).__init__()
        self.id = id
        self.content = content
