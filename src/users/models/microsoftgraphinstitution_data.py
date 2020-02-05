# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphinstitutionData(Model):
    """institutionData.

    :param description:
    :type description: str
    :param display_name:
    :type display_name: str
    :param location:
    :type location: ~users.models.MicrosoftgraphphysicalAddress
    :param web_url:
    :type web_url: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'location': {'key': 'location', 'type': 'MicrosoftgraphphysicalAddress'},
        'web_url': {'key': 'webUrl', 'type': 'str'},
    }

    def __init__(self, description=None, display_name=None, location=None, web_url=None):
        super(MicrosoftgraphinstitutionData, self).__init__()
        self.description = description
        self.display_name = display_name
        self.location = location
        self.web_url = web_url