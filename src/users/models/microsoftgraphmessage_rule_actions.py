# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphmessageRuleActions(Model):
    """messageRuleActions.

    :param move_to_folder:
    :type move_to_folder: str
    :param copy_to_folder:
    :type copy_to_folder: str
    :param delete:
    :type delete: bool
    :param permanent_delete:
    :type permanent_delete: bool
    :param mark_as_read:
    :type mark_as_read: bool
    :param mark_importance: Possible values include: 'low', 'normal', 'high'
    :type mark_importance: str or ~users.models.enum
    :param forward_to:
    :type forward_to: list[~users.models.Microsoftgraphrecipient]
    :param forward_as_attachment_to:
    :type forward_as_attachment_to:
     list[~users.models.Microsoftgraphrecipient]
    :param redirect_to:
    :type redirect_to: list[~users.models.Microsoftgraphrecipient]
    :param assign_categories:
    :type assign_categories: list[str]
    :param stop_processing_rules:
    :type stop_processing_rules: bool
    """

    _attribute_map = {
        'move_to_folder': {'key': 'moveToFolder', 'type': 'str'},
        'copy_to_folder': {'key': 'copyToFolder', 'type': 'str'},
        'delete': {'key': 'delete', 'type': 'bool'},
        'permanent_delete': {'key': 'permanentDelete', 'type': 'bool'},
        'mark_as_read': {'key': 'markAsRead', 'type': 'bool'},
        'mark_importance': {'key': 'markImportance', 'type': 'str'},
        'forward_to': {'key': 'forwardTo', 'type': '[Microsoftgraphrecipient]'},
        'forward_as_attachment_to': {'key': 'forwardAsAttachmentTo', 'type': '[Microsoftgraphrecipient]'},
        'redirect_to': {'key': 'redirectTo', 'type': '[Microsoftgraphrecipient]'},
        'assign_categories': {'key': 'assignCategories', 'type': '[str]'},
        'stop_processing_rules': {'key': 'stopProcessingRules', 'type': 'bool'},
    }

    def __init__(self, move_to_folder=None, copy_to_folder=None, delete=None, permanent_delete=None, mark_as_read=None, mark_importance=None, forward_to=None, forward_as_attachment_to=None, redirect_to=None, assign_categories=None, stop_processing_rules=None):
        super(MicrosoftgraphmessageRuleActions, self).__init__()
        self.move_to_folder = move_to_folder
        self.copy_to_folder = copy_to_folder
        self.delete = delete
        self.permanent_delete = permanent_delete
        self.mark_as_read = mark_as_read
        self.mark_importance = mark_importance
        self.forward_to = forward_to
        self.forward_as_attachment_to = forward_as_attachment_to
        self.redirect_to = redirect_to
        self.assign_categories = assign_categories
        self.stop_processing_rules = stop_processing_rules