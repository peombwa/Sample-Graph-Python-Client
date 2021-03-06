# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Microsoftgraphlocation(Model):
    """location.

    :param display_name:
    :type display_name: str
    :param location_email_address:
    :type location_email_address: str
    :param address:
    :type address: ~users.models.MicrosoftgraphphysicalAddress
    :param coordinates:
    :type coordinates: ~users.models.MicrosoftgraphoutlookGeoCoordinates
    :param location_uri:
    :type location_uri: str
    :param location_type: Possible values include: 'default',
     'conferenceRoom', 'homeAddress', 'businessAddress', 'geoCoordinates',
     'streetAddress', 'hotel', 'restaurant', 'localBusiness', 'postalAddress'
    :type location_type: str or ~users.models.enum
    :param unique_id:
    :type unique_id: str
    :param unique_id_type: Possible values include: 'unknown',
     'locationStore', 'directory', 'private', 'bing'
    :type unique_id_type: str or ~users.models.enum
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'location_email_address': {'key': 'locationEmailAddress', 'type': 'str'},
        'address': {'key': 'address', 'type': 'MicrosoftgraphphysicalAddress'},
        'coordinates': {'key': 'coordinates', 'type': 'MicrosoftgraphoutlookGeoCoordinates'},
        'location_uri': {'key': 'locationUri', 'type': 'str'},
        'location_type': {'key': 'locationType', 'type': 'str'},
        'unique_id': {'key': 'uniqueId', 'type': 'str'},
        'unique_id_type': {'key': 'uniqueIdType', 'type': 'str'},
    }

    def __init__(self, display_name=None, location_email_address=None, address=None, coordinates=None, location_uri=None, location_type=None, unique_id=None, unique_id_type=None):
        super(Microsoftgraphlocation, self).__init__()
        self.display_name = display_name
        self.location_email_address = location_email_address
        self.address = address
        self.coordinates = coordinates
        self.location_uri = location_uri
        self.location_type = location_type
        self.unique_id = unique_id
        self.unique_id_type = unique_id_type
