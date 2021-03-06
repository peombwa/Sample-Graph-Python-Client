# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphconfigurationManagerClientEnabledFeatures(Model):
    """configurationManagerClientEnabledFeatures.

    :param inventory: Whether inventory is managed by Intune
    :type inventory: bool
    :param modern_apps: Whether modern application is managed by Intune
    :type modern_apps: bool
    :param resource_access: Whether resource access is managed by Intune
    :type resource_access: bool
    :param device_configuration: Whether device configuration is managed by
     Intune
    :type device_configuration: bool
    :param compliance_policy: Whether compliance policy is managed by Intune
    :type compliance_policy: bool
    :param windows_update_for_business: Whether Windows Update for Business is
     managed by Intune
    :type windows_update_for_business: bool
    :param endpoint_protection: Whether Endpoint Protection is managed by
     Intune
    :type endpoint_protection: bool
    :param office_apps: Whether Office application is managed by Intune
    :type office_apps: bool
    """

    _attribute_map = {
        'inventory': {'key': 'inventory', 'type': 'bool'},
        'modern_apps': {'key': 'modernApps', 'type': 'bool'},
        'resource_access': {'key': 'resourceAccess', 'type': 'bool'},
        'device_configuration': {'key': 'deviceConfiguration', 'type': 'bool'},
        'compliance_policy': {'key': 'compliancePolicy', 'type': 'bool'},
        'windows_update_for_business': {'key': 'windowsUpdateForBusiness', 'type': 'bool'},
        'endpoint_protection': {'key': 'endpointProtection', 'type': 'bool'},
        'office_apps': {'key': 'officeApps', 'type': 'bool'},
    }

    def __init__(self, inventory=None, modern_apps=None, resource_access=None, device_configuration=None, compliance_policy=None, windows_update_for_business=None, endpoint_protection=None, office_apps=None):
        super(MicrosoftgraphconfigurationManagerClientEnabledFeatures, self).__init__()
        self.inventory = inventory
        self.modern_apps = modern_apps
        self.resource_access = resource_access
        self.device_configuration = device_configuration
        self.compliance_policy = compliance_policy
        self.windows_update_for_business = windows_update_for_business
        self.endpoint_protection = endpoint_protection
        self.office_apps = office_apps
