# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphWorkbookcommentallof1(Model):
    """workbookComment.

    :param content:
    :type content: str
    :param content_type:
    :type content_type: str
    :param replies:
    :type replies: list[~users.models.MicrosoftgraphworkbookCommentReply]
    """

    _attribute_map = {
        'content': {'key': 'content', 'type': 'str'},
        'content_type': {'key': 'contentType', 'type': 'str'},
        'replies': {'key': 'replies', 'type': '[MicrosoftgraphworkbookCommentReply]'},
    }

    def __init__(self, content=None, content_type=None, replies=None):
        super(ComponentsschemasmicrosoftGraphWorkbookcommentallof1, self).__init__()
        self.content = content
        self.content_type = content_type
        self.replies = replies
