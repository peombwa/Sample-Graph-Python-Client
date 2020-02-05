# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphDeviceconfigurationstateallof1(Model):
    """deviceConfigurationState.

    Device Configuration State for a given device.

    :param setting_states:
    :type setting_states:
     list[~users.models.MicrosoftgraphdeviceConfigurationSettingState]
    :param display_name: The name of the policy for this policyBase
    :type display_name: str
    :param version: The version of the policy
    :type version: int
    :param platform_type: Possible values include: 'android',
     'androidForWork', 'iOS', 'macOS', 'windowsPhone81', 'windows81AndLater',
     'windows10AndLater', 'androidWorkProfile', 'all'
    :type platform_type: str or ~users.models.enum
    :param state: Possible values include: 'unknown', 'notApplicable',
     'compliant', 'remediated', 'nonCompliant', 'error', 'conflict',
     'notAssigned'
    :type state: str or ~users.models.enum
    :param setting_count: Count of how many setting a policy holds
    :type setting_count: int
    :param user_id: User unique identifier, must be Guid
    :type user_id: str
    :param user_principal_name: User Principal Name
    :type user_principal_name: str
    """

    _validation = {
        'version': {'maximum': 2147483647, 'minimum': -2147483648},
        'setting_count': {'maximum': 2147483647, 'minimum': -2147483648},
    }

    _attribute_map = {
        'setting_states': {'key': 'settingStates', 'type': '[MicrosoftgraphdeviceConfigurationSettingState]'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'version': {'key': 'version', 'type': 'int'},
        'platform_type': {'key': 'platformType', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'setting_count': {'key': 'settingCount', 'type': 'int'},
        'user_id': {'key': 'userId', 'type': 'str'},
        'user_principal_name': {'key': 'userPrincipalName', 'type': 'str'},
    }

    def __init__(self, setting_states=None, display_name=None, version=None, platform_type=None, state=None, setting_count=None, user_id=None, user_principal_name=None):
        super(ComponentsschemasmicrosoftGraphDeviceconfigurationstateallof1, self).__init__()
        self.setting_states = setting_states
        self.display_name = display_name
        self.version = version
        self.platform_type = platform_type
        self.state = state
        self.setting_count = setting_count
        self.user_id = user_id
        self.user_principal_name = user_principal_name
