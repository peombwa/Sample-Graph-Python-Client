# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphMobileapptroubleshootingeventallof1(Model):
    """mobileAppTroubleshootingEvent.

    MobileAppTroubleshootingEvent Entity.

    :param managed_device_identifier: Device identifier created or collected
     by Intune.
    :type managed_device_identifier: str
    :param user_id: Identifier for the user that tried to enroll the device.
    :type user_id: str
    :param application_id: Intune application identifier.
    :type application_id: str
    :param history: Intune Mobile Application Troubleshooting History Item
    :type history:
     list[~users.models.MicrosoftgraphmobileAppTroubleshootingHistoryItem]
    :param app_log_collection_requests:
    :type app_log_collection_requests:
     list[~users.models.MicrosoftgraphappLogCollectionRequest]
    """

    _attribute_map = {
        'managed_device_identifier': {'key': 'managedDeviceIdentifier', 'type': 'str'},
        'user_id': {'key': 'userId', 'type': 'str'},
        'application_id': {'key': 'applicationId', 'type': 'str'},
        'history': {'key': 'history', 'type': '[MicrosoftgraphmobileAppTroubleshootingHistoryItem]'},
        'app_log_collection_requests': {'key': 'appLogCollectionRequests', 'type': '[MicrosoftgraphappLogCollectionRequest]'},
    }

    def __init__(self, managed_device_identifier=None, user_id=None, application_id=None, history=None, app_log_collection_requests=None):
        super(ComponentsschemasmicrosoftGraphMobileapptroubleshootingeventallof1, self).__init__()
        self.managed_device_identifier = managed_device_identifier
        self.user_id = user_id
        self.application_id = application_id
        self.history = history
        self.app_log_collection_requests = app_log_collection_requests
