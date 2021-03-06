# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphchatInfo(Model):
    """chatInfo.

    :param thread_id:
    :type thread_id: str
    :param message_id:
    :type message_id: str
    :param reply_chain_message_id:
    :type reply_chain_message_id: str
    """

    _attribute_map = {
        'thread_id': {'key': 'threadId', 'type': 'str'},
        'message_id': {'key': 'messageId', 'type': 'str'},
        'reply_chain_message_id': {'key': 'replyChainMessageId', 'type': 'str'},
    }

    def __init__(self, thread_id=None, message_id=None, reply_chain_message_id=None):
        super(MicrosoftgraphchatInfo, self).__init__()
        self.thread_id = thread_id
        self.message_id = message_id
        self.reply_chain_message_id = reply_chain_message_id
