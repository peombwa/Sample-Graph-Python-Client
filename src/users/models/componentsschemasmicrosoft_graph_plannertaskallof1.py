# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphPlannertaskallof1(Model):
    """plannerTask.

    :param created_by:
    :type created_by: ~users.models.MicrosoftgraphidentitySet
    :param plan_id:
    :type plan_id: str
    :param bucket_id:
    :type bucket_id: str
    :param title:
    :type title: str
    :param order_hint:
    :type order_hint: str
    :param assignee_priority:
    :type assignee_priority: str
    :param percent_complete:
    :type percent_complete: int
    :param priority:
    :type priority: int
    :param start_date_time:
    :type start_date_time: datetime
    :param created_date_time:
    :type created_date_time: datetime
    :param due_date_time:
    :type due_date_time: datetime
    :param has_description:
    :type has_description: bool
    :param preview_type: Possible values include: 'automatic', 'noPreview',
     'checklist', 'description', 'reference'
    :type preview_type: str or ~users.models.enum
    :param completed_date_time:
    :type completed_date_time: datetime
    :param completed_by:
    :type completed_by: ~users.models.MicrosoftgraphidentitySet
    :param reference_count:
    :type reference_count: int
    :param checklist_item_count:
    :type checklist_item_count: int
    :param active_checklist_item_count:
    :type active_checklist_item_count: int
    :param applied_categories:
    :type applied_categories: object
    :param assignments:
    :type assignments: object
    :param conversation_thread_id:
    :type conversation_thread_id: str
    :param details:
    :type details: ~users.models.MicrosoftgraphplannerTaskDetails
    :param assigned_to_task_board_format:
    :type assigned_to_task_board_format:
     ~users.models.MicrosoftgraphplannerAssignedToTaskBoardTaskFormat
    :param progress_task_board_format:
    :type progress_task_board_format:
     ~users.models.MicrosoftgraphplannerProgressTaskBoardTaskFormat
    :param bucket_task_board_format:
    :type bucket_task_board_format:
     ~users.models.MicrosoftgraphplannerBucketTaskBoardTaskFormat
    """

    _validation = {
        'percent_complete': {'maximum': 2147483647, 'minimum': -2147483648},
        'priority': {'maximum': 2147483647, 'minimum': -2147483648},
        'reference_count': {'maximum': 2147483647, 'minimum': -2147483648},
        'checklist_item_count': {'maximum': 2147483647, 'minimum': -2147483648},
        'active_checklist_item_count': {'maximum': 2147483647, 'minimum': -2147483648},
    }

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'MicrosoftgraphidentitySet'},
        'plan_id': {'key': 'planId', 'type': 'str'},
        'bucket_id': {'key': 'bucketId', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'order_hint': {'key': 'orderHint', 'type': 'str'},
        'assignee_priority': {'key': 'assigneePriority', 'type': 'str'},
        'percent_complete': {'key': 'percentComplete', 'type': 'int'},
        'priority': {'key': 'priority', 'type': 'int'},
        'start_date_time': {'key': 'startDateTime', 'type': 'iso-8601'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'due_date_time': {'key': 'dueDateTime', 'type': 'iso-8601'},
        'has_description': {'key': 'hasDescription', 'type': 'bool'},
        'preview_type': {'key': 'previewType', 'type': 'str'},
        'completed_date_time': {'key': 'completedDateTime', 'type': 'iso-8601'},
        'completed_by': {'key': 'completedBy', 'type': 'MicrosoftgraphidentitySet'},
        'reference_count': {'key': 'referenceCount', 'type': 'int'},
        'checklist_item_count': {'key': 'checklistItemCount', 'type': 'int'},
        'active_checklist_item_count': {'key': 'activeChecklistItemCount', 'type': 'int'},
        'applied_categories': {'key': 'appliedCategories', 'type': 'object'},
        'assignments': {'key': 'assignments', 'type': 'object'},
        'conversation_thread_id': {'key': 'conversationThreadId', 'type': 'str'},
        'details': {'key': 'details', 'type': 'MicrosoftgraphplannerTaskDetails'},
        'assigned_to_task_board_format': {'key': 'assignedToTaskBoardFormat', 'type': 'MicrosoftgraphplannerAssignedToTaskBoardTaskFormat'},
        'progress_task_board_format': {'key': 'progressTaskBoardFormat', 'type': 'MicrosoftgraphplannerProgressTaskBoardTaskFormat'},
        'bucket_task_board_format': {'key': 'bucketTaskBoardFormat', 'type': 'MicrosoftgraphplannerBucketTaskBoardTaskFormat'},
    }

    def __init__(self, created_by=None, plan_id=None, bucket_id=None, title=None, order_hint=None, assignee_priority=None, percent_complete=None, priority=None, start_date_time=None, created_date_time=None, due_date_time=None, has_description=None, preview_type=None, completed_date_time=None, completed_by=None, reference_count=None, checklist_item_count=None, active_checklist_item_count=None, applied_categories=None, assignments=None, conversation_thread_id=None, details=None, assigned_to_task_board_format=None, progress_task_board_format=None, bucket_task_board_format=None):
        super(ComponentsschemasmicrosoftGraphPlannertaskallof1, self).__init__()
        self.created_by = created_by
        self.plan_id = plan_id
        self.bucket_id = bucket_id
        self.title = title
        self.order_hint = order_hint
        self.assignee_priority = assignee_priority
        self.percent_complete = percent_complete
        self.priority = priority
        self.start_date_time = start_date_time
        self.created_date_time = created_date_time
        self.due_date_time = due_date_time
        self.has_description = has_description
        self.preview_type = preview_type
        self.completed_date_time = completed_date_time
        self.completed_by = completed_by
        self.reference_count = reference_count
        self.checklist_item_count = checklist_item_count
        self.active_checklist_item_count = active_checklist_item_count
        self.applied_categories = applied_categories
        self.assignments = assignments
        self.conversation_thread_id = conversation_thread_id
        self.details = details
        self.assigned_to_task_board_format = assigned_to_task_board_format
        self.progress_task_board_format = progress_task_board_format
        self.bucket_task_board_format = bucket_task_board_format
