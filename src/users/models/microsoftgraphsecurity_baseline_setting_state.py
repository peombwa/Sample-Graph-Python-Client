# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphsecurityBaselineSettingState(Model):
    """MicrosoftgraphsecurityBaselineSettingState.

    :param id:
    :type id: str
    :param setting_name: The setting name that is being reported
    :type setting_name: str
    :param state: Possible values include: 'unknown', 'secure',
     'notApplicable', 'notSecure', 'error', 'conflict'
    :type state: str or ~users.models.enum
    :param setting_category_id: The setting category id which this setting
     belongs to
    :type setting_category_id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'setting_name': {'key': 'settingName', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'setting_category_id': {'key': 'settingCategoryId', 'type': 'str'},
    }

    def __init__(self, id=None, setting_name=None, state=None, setting_category_id=None):
        super(MicrosoftgraphsecurityBaselineSettingState, self).__init__()
        self.id = id
        self.setting_name = setting_name
        self.state = state
        self.setting_category_id = setting_category_id
