# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphwindowsInformationProtectionDeviceRegistration(Model):
    """MicrosoftgraphwindowsInformationProtectionDeviceRegistration.

    :param id:
    :type id: str
    :param user_id: UserId associated with this device registration record.
    :type user_id: str
    :param device_registration_id: Device identifier for this device
     registration record.
    :type device_registration_id: str
    :param device_name: Device name.
    :type device_name: str
    :param device_type: Device type, for example, Windows laptop VS Windows
     phone.
    :type device_type: str
    :param device_mac_address: Device Mac address.
    :type device_mac_address: str
    :param last_check_in_date_time: Last checkin time of the device.
    :type last_check_in_date_time: datetime
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'user_id': {'key': 'userId', 'type': 'str'},
        'device_registration_id': {'key': 'deviceRegistrationId', 'type': 'str'},
        'device_name': {'key': 'deviceName', 'type': 'str'},
        'device_type': {'key': 'deviceType', 'type': 'str'},
        'device_mac_address': {'key': 'deviceMacAddress', 'type': 'str'},
        'last_check_in_date_time': {'key': 'lastCheckInDateTime', 'type': 'iso-8601'},
    }

    def __init__(self, id=None, user_id=None, device_registration_id=None, device_name=None, device_type=None, device_mac_address=None, last_check_in_date_time=None):
        super(MicrosoftgraphwindowsInformationProtectionDeviceRegistration, self).__init__()
        self.id = id
        self.user_id = user_id
        self.device_registration_id = device_registration_id
        self.device_name = device_name
        self.device_type = device_type
        self.device_mac_address = device_mac_address
        self.last_check_in_date_time = last_check_in_date_time