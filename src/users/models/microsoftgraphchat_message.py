# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphchatMessage(Model):
    """MicrosoftgraphchatMessage.

    :param id:
    :type id: str
    :param reply_to_id:
    :type reply_to_id: str
    :param from_property:
    :type from_property: ~users.models.MicrosoftgraphidentitySet
    :param etag:
    :type etag: str
    :param message_type: Possible values include: 'message', 'chatEvent',
     'typing'
    :type message_type: str or ~users.models.enum
    :param created_date_time:
    :type created_date_time: datetime
    :param last_modified_date_time:
    :type last_modified_date_time: datetime
    :param deleted_date_time:
    :type deleted_date_time: datetime
    :param subject:
    :type subject: str
    :param body:
    :type body: ~users.models.MicrosoftgraphitemBody
    :param summary:
    :type summary: str
    :param attachments:
    :type attachments: list[~users.models.MicrosoftgraphchatMessageAttachment]
    :param mentions:
    :type mentions: list[~users.models.MicrosoftgraphchatMessageMention]
    :param importance: Possible values include: 'normal', 'high', 'urgent'
    :type importance: str or ~users.models.enum
    :param policy_violation:
    :type policy_violation:
     ~users.models.MicrosoftgraphchatMessagePolicyViolation
    :param reactions:
    :type reactions: list[~users.models.MicrosoftgraphchatMessageReaction]
    :param locale:
    :type locale: str
    :param web_url:
    :type web_url: str
    :param replies:
    :type replies: list[~users.models.MicrosoftgraphchatMessage]
    :param hosted_contents:
    :type hosted_contents:
     list[~users.models.MicrosoftgraphchatMessageHostedContent]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'reply_to_id': {'key': 'replyToId', 'type': 'str'},
        'from_property': {'key': 'from', 'type': 'MicrosoftgraphidentitySet'},
        'etag': {'key': 'etag', 'type': 'str'},
        'message_type': {'key': 'messageType', 'type': 'str'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'last_modified_date_time': {'key': 'lastModifiedDateTime', 'type': 'iso-8601'},
        'deleted_date_time': {'key': 'deletedDateTime', 'type': 'iso-8601'},
        'subject': {'key': 'subject', 'type': 'str'},
        'body': {'key': 'body', 'type': 'MicrosoftgraphitemBody'},
        'summary': {'key': 'summary', 'type': 'str'},
        'attachments': {'key': 'attachments', 'type': '[MicrosoftgraphchatMessageAttachment]'},
        'mentions': {'key': 'mentions', 'type': '[MicrosoftgraphchatMessageMention]'},
        'importance': {'key': 'importance', 'type': 'str'},
        'policy_violation': {'key': 'policyViolation', 'type': 'MicrosoftgraphchatMessagePolicyViolation'},
        'reactions': {'key': 'reactions', 'type': '[MicrosoftgraphchatMessageReaction]'},
        'locale': {'key': 'locale', 'type': 'str'},
        'web_url': {'key': 'webUrl', 'type': 'str'},
        'replies': {'key': 'replies', 'type': '[MicrosoftgraphchatMessage]'},
        'hosted_contents': {'key': 'hostedContents', 'type': '[MicrosoftgraphchatMessageHostedContent]'},
    }

    def __init__(self, id=None, reply_to_id=None, from_property=None, etag=None, message_type=None, created_date_time=None, last_modified_date_time=None, deleted_date_time=None, subject=None, body=None, summary=None, attachments=None, mentions=None, importance=None, policy_violation=None, reactions=None, locale=None, web_url=None, replies=None, hosted_contents=None):
        super(MicrosoftgraphchatMessage, self).__init__()
        self.id = id
        self.reply_to_id = reply_to_id
        self.from_property = from_property
        self.etag = etag
        self.message_type = message_type
        self.created_date_time = created_date_time
        self.last_modified_date_time = last_modified_date_time
        self.deleted_date_time = deleted_date_time
        self.subject = subject
        self.body = body
        self.summary = summary
        self.attachments = attachments
        self.mentions = mentions
        self.importance = importance
        self.policy_violation = policy_violation
        self.reactions = reactions
        self.locale = locale
        self.web_url = web_url
        self.replies = replies
        self.hosted_contents = hosted_contents
