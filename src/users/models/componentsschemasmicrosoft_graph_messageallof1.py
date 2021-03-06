# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphMessageallof1(Model):
    """message.

    :param received_date_time:
    :type received_date_time: datetime
    :param sent_date_time:
    :type sent_date_time: datetime
    :param has_attachments:
    :type has_attachments: bool
    :param internet_message_id:
    :type internet_message_id: str
    :param internet_message_headers:
    :type internet_message_headers:
     list[~users.models.MicrosoftgraphinternetMessageHeader]
    :param subject:
    :type subject: str
    :param body:
    :type body: ~users.models.MicrosoftgraphitemBody
    :param body_preview:
    :type body_preview: str
    :param importance: Possible values include: 'low', 'normal', 'high'
    :type importance: str or ~users.models.enum
    :param parent_folder_id:
    :type parent_folder_id: str
    :param sender:
    :type sender: ~users.models.Microsoftgraphrecipient
    :param from_property:
    :type from_property: ~users.models.Microsoftgraphrecipient
    :param to_recipients:
    :type to_recipients: list[~users.models.Microsoftgraphrecipient]
    :param cc_recipients:
    :type cc_recipients: list[~users.models.Microsoftgraphrecipient]
    :param bcc_recipients:
    :type bcc_recipients: list[~users.models.Microsoftgraphrecipient]
    :param reply_to:
    :type reply_to: list[~users.models.Microsoftgraphrecipient]
    :param conversation_id:
    :type conversation_id: str
    :param conversation_index:
    :type conversation_index: bytes
    :param unique_body:
    :type unique_body: ~users.models.MicrosoftgraphitemBody
    :param is_delivery_receipt_requested:
    :type is_delivery_receipt_requested: bool
    :param is_read_receipt_requested:
    :type is_read_receipt_requested: bool
    :param is_read:
    :type is_read: bool
    :param is_draft:
    :type is_draft: bool
    :param web_link:
    :type web_link: str
    :param mentions_preview:
    :type mentions_preview: ~users.models.MicrosoftgraphmentionsPreview
    :param inference_classification: Possible values include: 'focused',
     'other'
    :type inference_classification: str or ~users.models.enum
    :param unsubscribe_data:
    :type unsubscribe_data: list[str]
    :param unsubscribe_enabled:
    :type unsubscribe_enabled: bool
    :param flag:
    :type flag: ~users.models.MicrosoftgraphfollowupFlag
    :param single_value_extended_properties:
    :type single_value_extended_properties:
     list[~users.models.MicrosoftgraphsingleValueLegacyExtendedProperty]
    :param multi_value_extended_properties:
    :type multi_value_extended_properties:
     list[~users.models.MicrosoftgraphmultiValueLegacyExtendedProperty]
    :param attachments:
    :type attachments: list[~users.models.Microsoftgraphattachment]
    :param extensions:
    :type extensions: list[~users.models.Microsoftgraphextension]
    :param mentions:
    :type mentions: list[~users.models.Microsoftgraphmention]
    """

    _attribute_map = {
        'received_date_time': {'key': 'receivedDateTime', 'type': 'iso-8601'},
        'sent_date_time': {'key': 'sentDateTime', 'type': 'iso-8601'},
        'has_attachments': {'key': 'hasAttachments', 'type': 'bool'},
        'internet_message_id': {'key': 'internetMessageId', 'type': 'str'},
        'internet_message_headers': {'key': 'internetMessageHeaders', 'type': '[MicrosoftgraphinternetMessageHeader]'},
        'subject': {'key': 'subject', 'type': 'str'},
        'body': {'key': 'body', 'type': 'MicrosoftgraphitemBody'},
        'body_preview': {'key': 'bodyPreview', 'type': 'str'},
        'importance': {'key': 'importance', 'type': 'str'},
        'parent_folder_id': {'key': 'parentFolderId', 'type': 'str'},
        'sender': {'key': 'sender', 'type': 'Microsoftgraphrecipient'},
        'from_property': {'key': 'from', 'type': 'Microsoftgraphrecipient'},
        'to_recipients': {'key': 'toRecipients', 'type': '[Microsoftgraphrecipient]'},
        'cc_recipients': {'key': 'ccRecipients', 'type': '[Microsoftgraphrecipient]'},
        'bcc_recipients': {'key': 'bccRecipients', 'type': '[Microsoftgraphrecipient]'},
        'reply_to': {'key': 'replyTo', 'type': '[Microsoftgraphrecipient]'},
        'conversation_id': {'key': 'conversationId', 'type': 'str'},
        'conversation_index': {'key': 'conversationIndex', 'type': 'base64'},
        'unique_body': {'key': 'uniqueBody', 'type': 'MicrosoftgraphitemBody'},
        'is_delivery_receipt_requested': {'key': 'isDeliveryReceiptRequested', 'type': 'bool'},
        'is_read_receipt_requested': {'key': 'isReadReceiptRequested', 'type': 'bool'},
        'is_read': {'key': 'isRead', 'type': 'bool'},
        'is_draft': {'key': 'isDraft', 'type': 'bool'},
        'web_link': {'key': 'webLink', 'type': 'str'},
        'mentions_preview': {'key': 'mentionsPreview', 'type': 'MicrosoftgraphmentionsPreview'},
        'inference_classification': {'key': 'inferenceClassification', 'type': 'str'},
        'unsubscribe_data': {'key': 'unsubscribeData', 'type': '[str]'},
        'unsubscribe_enabled': {'key': 'unsubscribeEnabled', 'type': 'bool'},
        'flag': {'key': 'flag', 'type': 'MicrosoftgraphfollowupFlag'},
        'single_value_extended_properties': {'key': 'singleValueExtendedProperties', 'type': '[MicrosoftgraphsingleValueLegacyExtendedProperty]'},
        'multi_value_extended_properties': {'key': 'multiValueExtendedProperties', 'type': '[MicrosoftgraphmultiValueLegacyExtendedProperty]'},
        'attachments': {'key': 'attachments', 'type': '[Microsoftgraphattachment]'},
        'extensions': {'key': 'extensions', 'type': '[Microsoftgraphextension]'},
        'mentions': {'key': 'mentions', 'type': '[Microsoftgraphmention]'},
    }

    def __init__(self, received_date_time=None, sent_date_time=None, has_attachments=None, internet_message_id=None, internet_message_headers=None, subject=None, body=None, body_preview=None, importance=None, parent_folder_id=None, sender=None, from_property=None, to_recipients=None, cc_recipients=None, bcc_recipients=None, reply_to=None, conversation_id=None, conversation_index=None, unique_body=None, is_delivery_receipt_requested=None, is_read_receipt_requested=None, is_read=None, is_draft=None, web_link=None, mentions_preview=None, inference_classification=None, unsubscribe_data=None, unsubscribe_enabled=None, flag=None, single_value_extended_properties=None, multi_value_extended_properties=None, attachments=None, extensions=None, mentions=None):
        super(ComponentsschemasmicrosoftGraphMessageallof1, self).__init__()
        self.received_date_time = received_date_time
        self.sent_date_time = sent_date_time
        self.has_attachments = has_attachments
        self.internet_message_id = internet_message_id
        self.internet_message_headers = internet_message_headers
        self.subject = subject
        self.body = body
        self.body_preview = body_preview
        self.importance = importance
        self.parent_folder_id = parent_folder_id
        self.sender = sender
        self.from_property = from_property
        self.to_recipients = to_recipients
        self.cc_recipients = cc_recipients
        self.bcc_recipients = bcc_recipients
        self.reply_to = reply_to
        self.conversation_id = conversation_id
        self.conversation_index = conversation_index
        self.unique_body = unique_body
        self.is_delivery_receipt_requested = is_delivery_receipt_requested
        self.is_read_receipt_requested = is_read_receipt_requested
        self.is_read = is_read
        self.is_draft = is_draft
        self.web_link = web_link
        self.mentions_preview = mentions_preview
        self.inference_classification = inference_classification
        self.unsubscribe_data = unsubscribe_data
        self.unsubscribe_enabled = unsubscribe_enabled
        self.flag = flag
        self.single_value_extended_properties = single_value_extended_properties
        self.multi_value_extended_properties = multi_value_extended_properties
        self.attachments = attachments
        self.extensions = extensions
        self.mentions = mentions
