# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphmessageRule(Model):
    """MicrosoftgraphmessageRule.

    :param id:
    :type id: str
    :param display_name:
    :type display_name: str
    :param sequence:
    :type sequence: int
    :param conditions:
    :type conditions: ~users.models.MicrosoftgraphmessageRulePredicates
    :param actions:
    :type actions: ~users.models.MicrosoftgraphmessageRuleActions
    :param exceptions:
    :type exceptions: ~users.models.MicrosoftgraphmessageRulePredicates
    :param is_enabled:
    :type is_enabled: bool
    :param has_error:
    :type has_error: bool
    :param is_read_only:
    :type is_read_only: bool
    """

    _validation = {
        'sequence': {'maximum': 2147483647, 'minimum': -2147483648},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'sequence': {'key': 'sequence', 'type': 'int'},
        'conditions': {'key': 'conditions', 'type': 'MicrosoftgraphmessageRulePredicates'},
        'actions': {'key': 'actions', 'type': 'MicrosoftgraphmessageRuleActions'},
        'exceptions': {'key': 'exceptions', 'type': 'MicrosoftgraphmessageRulePredicates'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'has_error': {'key': 'hasError', 'type': 'bool'},
        'is_read_only': {'key': 'isReadOnly', 'type': 'bool'},
    }

    def __init__(self, id=None, display_name=None, sequence=None, conditions=None, actions=None, exceptions=None, is_enabled=None, has_error=None, is_read_only=None):
        super(MicrosoftgraphmessageRule, self).__init__()
        self.id = id
        self.display_name = display_name
        self.sequence = sequence
        self.conditions = conditions
        self.actions = actions
        self.exceptions = exceptions
        self.is_enabled = is_enabled
        self.has_error = has_error
        self.is_read_only = is_read_only
