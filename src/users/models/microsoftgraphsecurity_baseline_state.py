# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphsecurityBaselineState(Model):
    """MicrosoftgraphsecurityBaselineState.

    :param id:
    :type id: str
    :param security_baseline_template_id: The security baseline template id
    :type security_baseline_template_id: str
    :param display_name: The display name of the security baseline
    :type display_name: str
    :param setting_states:
    :type setting_states:
     list[~users.models.MicrosoftgraphsecurityBaselineSettingState]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'security_baseline_template_id': {'key': 'securityBaselineTemplateId', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'setting_states': {'key': 'settingStates', 'type': '[MicrosoftgraphsecurityBaselineSettingState]'},
    }

    def __init__(self, id=None, security_baseline_template_id=None, display_name=None, setting_states=None):
        super(MicrosoftgraphsecurityBaselineState, self).__init__()
        self.id = id
        self.security_baseline_template_id = security_baseline_template_id
        self.display_name = display_name
        self.setting_states = setting_states
