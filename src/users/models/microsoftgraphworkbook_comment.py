# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphworkbookComment(Model):
    """MicrosoftgraphworkbookComment.

    :param id:
    :type id: str
    :param content:
    :type content: str
    :param content_type:
    :type content_type: str
    :param replies:
    :type replies: list[~users.models.MicrosoftgraphworkbookCommentReply]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'content': {'key': 'content', 'type': 'str'},
        'content_type': {'key': 'contentType', 'type': 'str'},
        'replies': {'key': 'replies', 'type': '[MicrosoftgraphworkbookCommentReply]'},
    }

    def __init__(self, id=None, content=None, content_type=None, replies=None):
        super(MicrosoftgraphworkbookComment, self).__init__()
        self.id = id
        self.content = content
        self.content_type = content_type
        self.replies = replies
