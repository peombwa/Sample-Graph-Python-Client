# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphEventallof1(Model):
    """event.

    :param original_start_time_zone:
    :type original_start_time_zone: str
    :param original_end_time_zone:
    :type original_end_time_zone: str
    :param response_status:
    :type response_status: ~users.models.MicrosoftgraphresponseStatus
    :param uid:
    :type uid: str
    :param reminder_minutes_before_start:
    :type reminder_minutes_before_start: int
    :param is_reminder_on:
    :type is_reminder_on: bool
    :param has_attachments:
    :type has_attachments: bool
    :param subject:
    :type subject: str
    :param body:
    :type body: ~users.models.MicrosoftgraphitemBody
    :param body_preview:
    :type body_preview: str
    :param importance: Possible values include: 'low', 'normal', 'high'
    :type importance: str or ~users.models.enum
    :param sensitivity: Possible values include: 'normal', 'personal',
     'private', 'confidential'
    :type sensitivity: str or ~users.models.enum
    :param start:
    :type start: ~users.models.MicrosoftgraphdateTimeTimeZone
    :param original_start:
    :type original_start: datetime
    :param end:
    :type end: ~users.models.MicrosoftgraphdateTimeTimeZone
    :param location:
    :type location: ~users.models.Microsoftgraphlocation
    :param locations:
    :type locations: list[~users.models.Microsoftgraphlocation]
    :param is_all_day:
    :type is_all_day: bool
    :param is_cancelled:
    :type is_cancelled: bool
    :param is_organizer:
    :type is_organizer: bool
    :param recurrence:
    :type recurrence: ~users.models.MicrosoftgraphpatternedRecurrence
    :param response_requested:
    :type response_requested: bool
    :param series_master_id:
    :type series_master_id: str
    :param show_as: Possible values include: 'free', 'tentative', 'busy',
     'oof', 'workingElsewhere', 'unknown'
    :type show_as: str or ~users.models.enum
    :param type: Possible values include: 'singleInstance', 'occurrence',
     'exception', 'seriesMaster'
    :type type: str or ~users.models.enum
    :param attendees:
    :type attendees: list[~users.models.Microsoftgraphattendee]
    :param organizer:
    :type organizer: ~users.models.Microsoftgraphrecipient
    :param web_link:
    :type web_link: str
    :param online_meeting_url:
    :type online_meeting_url: str
    :param is_online_meeting:
    :type is_online_meeting: bool
    :param online_meeting_provider: Possible values include: 'unknown',
     'skypeForBusiness', 'skypeForConsumer', 'teamsForBusiness'
    :type online_meeting_provider: str or ~users.models.enum
    :param online_meeting:
    :type online_meeting: ~users.models.MicrosoftgraphonlineMeetingInfo
    :param allow_new_time_proposals:
    :type allow_new_time_proposals: bool
    :param attachments:
    :type attachments: list[~users.models.Microsoftgraphattachment]
    :param single_value_extended_properties:
    :type single_value_extended_properties:
     list[~users.models.MicrosoftgraphsingleValueLegacyExtendedProperty]
    :param multi_value_extended_properties:
    :type multi_value_extended_properties:
     list[~users.models.MicrosoftgraphmultiValueLegacyExtendedProperty]
    :param calendar:
    :type calendar: ~users.models.Microsoftgraphcalendar
    :param instances:
    :type instances: list[~users.models.Microsoftgraphevent]
    :param extensions:
    :type extensions: list[~users.models.Microsoftgraphextension]
    """

    _validation = {
        'reminder_minutes_before_start': {'maximum': 2147483647, 'minimum': -2147483648},
    }

    _attribute_map = {
        'original_start_time_zone': {'key': 'originalStartTimeZone', 'type': 'str'},
        'original_end_time_zone': {'key': 'originalEndTimeZone', 'type': 'str'},
        'response_status': {'key': 'responseStatus', 'type': 'MicrosoftgraphresponseStatus'},
        'uid': {'key': 'uid', 'type': 'str'},
        'reminder_minutes_before_start': {'key': 'reminderMinutesBeforeStart', 'type': 'int'},
        'is_reminder_on': {'key': 'isReminderOn', 'type': 'bool'},
        'has_attachments': {'key': 'hasAttachments', 'type': 'bool'},
        'subject': {'key': 'subject', 'type': 'str'},
        'body': {'key': 'body', 'type': 'MicrosoftgraphitemBody'},
        'body_preview': {'key': 'bodyPreview', 'type': 'str'},
        'importance': {'key': 'importance', 'type': 'str'},
        'sensitivity': {'key': 'sensitivity', 'type': 'str'},
        'start': {'key': 'start', 'type': 'MicrosoftgraphdateTimeTimeZone'},
        'original_start': {'key': 'originalStart', 'type': 'iso-8601'},
        'end': {'key': 'end', 'type': 'MicrosoftgraphdateTimeTimeZone'},
        'location': {'key': 'location', 'type': 'Microsoftgraphlocation'},
        'locations': {'key': 'locations', 'type': '[Microsoftgraphlocation]'},
        'is_all_day': {'key': 'isAllDay', 'type': 'bool'},
        'is_cancelled': {'key': 'isCancelled', 'type': 'bool'},
        'is_organizer': {'key': 'isOrganizer', 'type': 'bool'},
        'recurrence': {'key': 'recurrence', 'type': 'MicrosoftgraphpatternedRecurrence'},
        'response_requested': {'key': 'responseRequested', 'type': 'bool'},
        'series_master_id': {'key': 'seriesMasterId', 'type': 'str'},
        'show_as': {'key': 'showAs', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'attendees': {'key': 'attendees', 'type': '[Microsoftgraphattendee]'},
        'organizer': {'key': 'organizer', 'type': 'Microsoftgraphrecipient'},
        'web_link': {'key': 'webLink', 'type': 'str'},
        'online_meeting_url': {'key': 'onlineMeetingUrl', 'type': 'str'},
        'is_online_meeting': {'key': 'isOnlineMeeting', 'type': 'bool'},
        'online_meeting_provider': {'key': 'onlineMeetingProvider', 'type': 'str'},
        'online_meeting': {'key': 'onlineMeeting', 'type': 'MicrosoftgraphonlineMeetingInfo'},
        'allow_new_time_proposals': {'key': 'allowNewTimeProposals', 'type': 'bool'},
        'attachments': {'key': 'attachments', 'type': '[Microsoftgraphattachment]'},
        'single_value_extended_properties': {'key': 'singleValueExtendedProperties', 'type': '[MicrosoftgraphsingleValueLegacyExtendedProperty]'},
        'multi_value_extended_properties': {'key': 'multiValueExtendedProperties', 'type': '[MicrosoftgraphmultiValueLegacyExtendedProperty]'},
        'calendar': {'key': 'calendar', 'type': 'Microsoftgraphcalendar'},
        'instances': {'key': 'instances', 'type': '[Microsoftgraphevent]'},
        'extensions': {'key': 'extensions', 'type': '[Microsoftgraphextension]'},
    }

    def __init__(self, original_start_time_zone=None, original_end_time_zone=None, response_status=None, uid=None, reminder_minutes_before_start=None, is_reminder_on=None, has_attachments=None, subject=None, body=None, body_preview=None, importance=None, sensitivity=None, start=None, original_start=None, end=None, location=None, locations=None, is_all_day=None, is_cancelled=None, is_organizer=None, recurrence=None, response_requested=None, series_master_id=None, show_as=None, type=None, attendees=None, organizer=None, web_link=None, online_meeting_url=None, is_online_meeting=None, online_meeting_provider=None, online_meeting=None, allow_new_time_proposals=None, attachments=None, single_value_extended_properties=None, multi_value_extended_properties=None, calendar=None, instances=None, extensions=None):
        super(ComponentsschemasmicrosoftGraphEventallof1, self).__init__()
        self.original_start_time_zone = original_start_time_zone
        self.original_end_time_zone = original_end_time_zone
        self.response_status = response_status
        self.uid = uid
        self.reminder_minutes_before_start = reminder_minutes_before_start
        self.is_reminder_on = is_reminder_on
        self.has_attachments = has_attachments
        self.subject = subject
        self.body = body
        self.body_preview = body_preview
        self.importance = importance
        self.sensitivity = sensitivity
        self.start = start
        self.original_start = original_start
        self.end = end
        self.location = location
        self.locations = locations
        self.is_all_day = is_all_day
        self.is_cancelled = is_cancelled
        self.is_organizer = is_organizer
        self.recurrence = recurrence
        self.response_requested = response_requested
        self.series_master_id = series_master_id
        self.show_as = show_as
        self.type = type
        self.attendees = attendees
        self.organizer = organizer
        self.web_link = web_link
        self.online_meeting_url = online_meeting_url
        self.is_online_meeting = is_online_meeting
        self.online_meeting_provider = online_meeting_provider
        self.online_meeting = online_meeting
        self.allow_new_time_proposals = allow_new_time_proposals
        self.attachments = attachments
        self.single_value_extended_properties = single_value_extended_properties
        self.multi_value_extended_properties = multi_value_extended_properties
        self.calendar = calendar
        self.instances = instances
        self.extensions = extensions
