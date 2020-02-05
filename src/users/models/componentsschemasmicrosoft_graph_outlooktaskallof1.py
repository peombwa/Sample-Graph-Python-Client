# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphOutlooktaskallof1(Model):
    """outlookTask.

    :param assigned_to:
    :type assigned_to: str
    :param body:
    :type body: ~users.models.MicrosoftgraphitemBody
    :param completed_date_time:
    :type completed_date_time: ~users.models.MicrosoftgraphdateTimeTimeZone
    :param due_date_time:
    :type due_date_time: ~users.models.MicrosoftgraphdateTimeTimeZone
    :param has_attachments:
    :type has_attachments: bool
    :param importance: Possible values include: 'low', 'normal', 'high'
    :type importance: str or ~users.models.enum
    :param is_reminder_on:
    :type is_reminder_on: bool
    :param owner:
    :type owner: str
    :param parent_folder_id:
    :type parent_folder_id: str
    :param recurrence:
    :type recurrence: ~users.models.MicrosoftgraphpatternedRecurrence
    :param reminder_date_time:
    :type reminder_date_time: ~users.models.MicrosoftgraphdateTimeTimeZone
    :param sensitivity: Possible values include: 'normal', 'personal',
     'private', 'confidential'
    :type sensitivity: str or ~users.models.enum
    :param start_date_time:
    :type start_date_time: ~users.models.MicrosoftgraphdateTimeTimeZone
    :param status: Possible values include: 'notStarted', 'inProgress',
     'completed', 'waitingOnOthers', 'deferred'
    :type status: str or ~users.models.enum
    :param subject:
    :type subject: str
    :param single_value_extended_properties:
    :type single_value_extended_properties:
     list[~users.models.MicrosoftgraphsingleValueLegacyExtendedProperty]
    :param multi_value_extended_properties:
    :type multi_value_extended_properties:
     list[~users.models.MicrosoftgraphmultiValueLegacyExtendedProperty]
    :param attachments:
    :type attachments: list[~users.models.Microsoftgraphattachment]
    """

    _attribute_map = {
        'assigned_to': {'key': 'assignedTo', 'type': 'str'},
        'body': {'key': 'body', 'type': 'MicrosoftgraphitemBody'},
        'completed_date_time': {'key': 'completedDateTime', 'type': 'MicrosoftgraphdateTimeTimeZone'},
        'due_date_time': {'key': 'dueDateTime', 'type': 'MicrosoftgraphdateTimeTimeZone'},
        'has_attachments': {'key': 'hasAttachments', 'type': 'bool'},
        'importance': {'key': 'importance', 'type': 'str'},
        'is_reminder_on': {'key': 'isReminderOn', 'type': 'bool'},
        'owner': {'key': 'owner', 'type': 'str'},
        'parent_folder_id': {'key': 'parentFolderId', 'type': 'str'},
        'recurrence': {'key': 'recurrence', 'type': 'MicrosoftgraphpatternedRecurrence'},
        'reminder_date_time': {'key': 'reminderDateTime', 'type': 'MicrosoftgraphdateTimeTimeZone'},
        'sensitivity': {'key': 'sensitivity', 'type': 'str'},
        'start_date_time': {'key': 'startDateTime', 'type': 'MicrosoftgraphdateTimeTimeZone'},
        'status': {'key': 'status', 'type': 'str'},
        'subject': {'key': 'subject', 'type': 'str'},
        'single_value_extended_properties': {'key': 'singleValueExtendedProperties', 'type': '[MicrosoftgraphsingleValueLegacyExtendedProperty]'},
        'multi_value_extended_properties': {'key': 'multiValueExtendedProperties', 'type': '[MicrosoftgraphmultiValueLegacyExtendedProperty]'},
        'attachments': {'key': 'attachments', 'type': '[Microsoftgraphattachment]'},
    }

    def __init__(self, assigned_to=None, body=None, completed_date_time=None, due_date_time=None, has_attachments=None, importance=None, is_reminder_on=None, owner=None, parent_folder_id=None, recurrence=None, reminder_date_time=None, sensitivity=None, start_date_time=None, status=None, subject=None, single_value_extended_properties=None, multi_value_extended_properties=None, attachments=None):
        super(ComponentsschemasmicrosoftGraphOutlooktaskallof1, self).__init__()
        self.assigned_to = assigned_to
        self.body = body
        self.completed_date_time = completed_date_time
        self.due_date_time = due_date_time
        self.has_attachments = has_attachments
        self.importance = importance
        self.is_reminder_on = is_reminder_on
        self.owner = owner
        self.parent_folder_id = parent_folder_id
        self.recurrence = recurrence
        self.reminder_date_time = reminder_date_time
        self.sensitivity = sensitivity
        self.start_date_time = start_date_time
        self.status = status
        self.subject = subject
        self.single_value_extended_properties = single_value_extended_properties
        self.multi_value_extended_properties = multi_value_extended_properties
        self.attachments = attachments