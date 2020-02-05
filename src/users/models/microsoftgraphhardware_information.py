# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphhardwareInformation(Model):
    """hardwareInformation.

    :param serial_number: Serial number.
    :type serial_number: str
    :param total_storage_space: Total storage space of the device.
    :type total_storage_space: long
    :param free_storage_space: Free storage space of the device.
    :type free_storage_space: long
    :param imei: IMEI
    :type imei: str
    :param meid: MEID
    :type meid: str
    :param manufacturer: Manufacturer of the device
    :type manufacturer: str
    :param model: Model of the device
    :type model: str
    :param phone_number: Phone number of the device
    :type phone_number: str
    :param subscriber_carrier: Subscriber carrier of the device
    :type subscriber_carrier: str
    :param cellular_technology: Cellular technology of the device
    :type cellular_technology: str
    :param wifi_mac: WiFi MAC address of the device
    :type wifi_mac: str
    :param operating_system_language: Operating system language of the device
    :type operating_system_language: str
    :param is_supervised: Supervised mode of the device
    :type is_supervised: bool
    :param is_encrypted: Encryption status of the device
    :type is_encrypted: bool
    :param is_shared_device: Shared iPad
    :type is_shared_device: bool
    :param shared_device_cached_users: All users on the shared Apple device
    :type shared_device_cached_users:
     list[~users.models.MicrosoftgraphsharedAppleDeviceUser]
    :param tpm_specification_version: String that specifies the specification
     version.
    :type tpm_specification_version: str
    :param operating_system_edition: String that specifies the OS edition.
    :type operating_system_edition: str
    :param device_full_qualified_domain_name: Returns the fully qualified
     domain name of the device (if any). If the device is not domain-joined, it
     returns an empty string.
    :type device_full_qualified_domain_name: str
    :param
     device_guard_virtualization_based_security_hardware_requirement_state:
     Possible values include: 'meetHardwareRequirements', 'secureBootRequired',
     'dmaProtectionRequired', 'hyperVNotSupportedForGuestVM',
     'hyperVNotAvailable'
    :type
     device_guard_virtualization_based_security_hardware_requirement_state: str
     or ~users.models.enum
    :param device_guard_virtualization_based_security_state: Possible values
     include: 'running', 'rebootRequired', 'require64BitArchitecture',
     'notLicensed', 'notConfigured', 'doesNotMeetHardwareRequirements', 'other'
    :type device_guard_virtualization_based_security_state: str or
     ~users.models.enum
    :param device_guard_local_system_authority_credential_guard_state:
     Possible values include: 'running', 'rebootRequired', 'notLicensed',
     'notConfigured', 'virtualizationBasedSecurityNotRunning'
    :type device_guard_local_system_authority_credential_guard_state: str or
     ~users.models.enum
    :param os_build_number: Operating System Build Number on Android device
    :type os_build_number: str
    """

    _attribute_map = {
        'serial_number': {'key': 'serialNumber', 'type': 'str'},
        'total_storage_space': {'key': 'totalStorageSpace', 'type': 'long'},
        'free_storage_space': {'key': 'freeStorageSpace', 'type': 'long'},
        'imei': {'key': 'imei', 'type': 'str'},
        'meid': {'key': 'meid', 'type': 'str'},
        'manufacturer': {'key': 'manufacturer', 'type': 'str'},
        'model': {'key': 'model', 'type': 'str'},
        'phone_number': {'key': 'phoneNumber', 'type': 'str'},
        'subscriber_carrier': {'key': 'subscriberCarrier', 'type': 'str'},
        'cellular_technology': {'key': 'cellularTechnology', 'type': 'str'},
        'wifi_mac': {'key': 'wifiMac', 'type': 'str'},
        'operating_system_language': {'key': 'operatingSystemLanguage', 'type': 'str'},
        'is_supervised': {'key': 'isSupervised', 'type': 'bool'},
        'is_encrypted': {'key': 'isEncrypted', 'type': 'bool'},
        'is_shared_device': {'key': 'isSharedDevice', 'type': 'bool'},
        'shared_device_cached_users': {'key': 'sharedDeviceCachedUsers', 'type': '[MicrosoftgraphsharedAppleDeviceUser]'},
        'tpm_specification_version': {'key': 'tpmSpecificationVersion', 'type': 'str'},
        'operating_system_edition': {'key': 'operatingSystemEdition', 'type': 'str'},
        'device_full_qualified_domain_name': {'key': 'deviceFullQualifiedDomainName', 'type': 'str'},
        'device_guard_virtualization_based_security_hardware_requirement_state': {'key': 'deviceGuardVirtualizationBasedSecurityHardwareRequirementState', 'type': 'str'},
        'device_guard_virtualization_based_security_state': {'key': 'deviceGuardVirtualizationBasedSecurityState', 'type': 'str'},
        'device_guard_local_system_authority_credential_guard_state': {'key': 'deviceGuardLocalSystemAuthorityCredentialGuardState', 'type': 'str'},
        'os_build_number': {'key': 'osBuildNumber', 'type': 'str'},
    }

    def __init__(self, serial_number=None, total_storage_space=None, free_storage_space=None, imei=None, meid=None, manufacturer=None, model=None, phone_number=None, subscriber_carrier=None, cellular_technology=None, wifi_mac=None, operating_system_language=None, is_supervised=None, is_encrypted=None, is_shared_device=None, shared_device_cached_users=None, tpm_specification_version=None, operating_system_edition=None, device_full_qualified_domain_name=None, device_guard_virtualization_based_security_hardware_requirement_state=None, device_guard_virtualization_based_security_state=None, device_guard_local_system_authority_credential_guard_state=None, os_build_number=None):
        super(MicrosoftgraphhardwareInformation, self).__init__()
        self.serial_number = serial_number
        self.total_storage_space = total_storage_space
        self.free_storage_space = free_storage_space
        self.imei = imei
        self.meid = meid
        self.manufacturer = manufacturer
        self.model = model
        self.phone_number = phone_number
        self.subscriber_carrier = subscriber_carrier
        self.cellular_technology = cellular_technology
        self.wifi_mac = wifi_mac
        self.operating_system_language = operating_system_language
        self.is_supervised = is_supervised
        self.is_encrypted = is_encrypted
        self.is_shared_device = is_shared_device
        self.shared_device_cached_users = shared_device_cached_users
        self.tpm_specification_version = tpm_specification_version
        self.operating_system_edition = operating_system_edition
        self.device_full_qualified_domain_name = device_full_qualified_domain_name
        self.device_guard_virtualization_based_security_hardware_requirement_state = device_guard_virtualization_based_security_hardware_requirement_state
        self.device_guard_virtualization_based_security_state = device_guard_virtualization_based_security_state
        self.device_guard_local_system_authority_credential_guard_state = device_guard_local_system_authority_credential_guard_state
        self.os_build_number = os_build_number
