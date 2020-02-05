# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphdeviceCompliancePolicySettingState(Model):
    """deviceCompliancePolicySettingState.

    :param setting: The setting that is being reported
    :type setting: str
    :param setting_name: Localized/user friendly setting name that is being
     reported
    :type setting_name: str
    :param instance_display_name: Name of setting instance that is being
     reported.
    :type instance_display_name: str
    :param state: Possible values include: 'unknown', 'notApplicable',
     'compliant', 'remediated', 'nonCompliant', 'error', 'conflict',
     'notAssigned'
    :type state: str or ~users.models.enum
    :param error_code: Error code for the setting
    :type error_code: long
    :param error_description: Error description
    :type error_description: str
    :param user_id: UserId
    :type user_id: str
    :param user_name: UserName
    :type user_name: str
    :param user_email: UserEmail
    :type user_email: str
    :param user_principal_name: UserPrincipalName.
    :type user_principal_name: str
    :param sources: Contributing policies
    :type sources: list[~users.models.MicrosoftgraphsettingSource]
    :param current_value: Current value of setting on device
    :type current_value: str
    """

    _attribute_map = {
        'setting': {'key': 'setting', 'type': 'str'},
        'setting_name': {'key': 'settingName', 'type': 'str'},
        'instance_display_name': {'key': 'instanceDisplayName', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'error_code': {'key': 'errorCode', 'type': 'long'},
        'error_description': {'key': 'errorDescription', 'type': 'str'},
        'user_id': {'key': 'userId', 'type': 'str'},
        'user_name': {'key': 'userName', 'type': 'str'},
        'user_email': {'key': 'userEmail', 'type': 'str'},
        'user_principal_name': {'key': 'userPrincipalName', 'type': 'str'},
        'sources': {'key': 'sources', 'type': '[MicrosoftgraphsettingSource]'},
        'current_value': {'key': 'currentValue', 'type': 'str'},
    }

    def __init__(self, setting=None, setting_name=None, instance_display_name=None, state=None, error_code=None, error_description=None, user_id=None, user_name=None, user_email=None, user_principal_name=None, sources=None, current_value=None):
        super(MicrosoftgraphdeviceCompliancePolicySettingState, self).__init__()
        self.setting = setting
        self.setting_name = setting_name
        self.instance_display_name = instance_display_name
        self.state = state
        self.error_code = error_code
        self.error_description = error_description
        self.user_id = user_id
        self.user_name = user_name
        self.user_email = user_email
        self.user_principal_name = user_principal_name
        self.sources = sources
        self.current_value = current_value
