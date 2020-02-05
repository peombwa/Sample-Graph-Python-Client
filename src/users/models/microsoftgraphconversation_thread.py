# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphconversationThread(Model):
    """MicrosoftgraphconversationThread.

    :param id:
    :type id: str
    :param to_recipients:
    :type to_recipients: list[~users.models.Microsoftgraphrecipient]
    :param topic:
    :type topic: str
    :param has_attachments:
    :type has_attachments: bool
    :param last_delivered_date_time:
    :type last_delivered_date_time: datetime
    :param unique_senders:
    :type unique_senders: list[str]
    :param cc_recipients:
    :type cc_recipients: list[~users.models.Microsoftgraphrecipient]
    :param preview:
    :type preview: str
    :param is_locked:
    :type is_locked: bool
    :param posts:
    :type posts: list[~users.models.Microsoftgraphpost]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'to_recipients': {'key': 'toRecipients', 'type': '[Microsoftgraphrecipient]'},
        'topic': {'key': 'topic', 'type': 'str'},
        'has_attachments': {'key': 'hasAttachments', 'type': 'bool'},
        'last_delivered_date_time': {'key': 'lastDeliveredDateTime', 'type': 'iso-8601'},
        'unique_senders': {'key': 'uniqueSenders', 'type': '[str]'},
        'cc_recipients': {'key': 'ccRecipients', 'type': '[Microsoftgraphrecipient]'},
        'preview': {'key': 'preview', 'type': 'str'},
        'is_locked': {'key': 'isLocked', 'type': 'bool'},
        'posts': {'key': 'posts', 'type': '[Microsoftgraphpost]'},
    }

    def __init__(self, id=None, to_recipients=None, topic=None, has_attachments=None, last_delivered_date_time=None, unique_senders=None, cc_recipients=None, preview=None, is_locked=None, posts=None):
        super(MicrosoftgraphconversationThread, self).__init__()
        self.id = id
        self.to_recipients = to_recipients
        self.topic = topic
        self.has_attachments = has_attachments
        self.last_delivered_date_time = last_delivered_date_time
        self.unique_senders = unique_senders
        self.cc_recipients = cc_recipients
        self.preview = preview
        self.is_locked = is_locked
        self.posts = posts
