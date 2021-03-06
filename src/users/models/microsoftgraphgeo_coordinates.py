# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphgeoCoordinates(Model):
    """geoCoordinates.

    :param altitude:
    :type altitude: float
    :param latitude:
    :type latitude: float
    :param longitude:
    :type longitude: float
    """

    _attribute_map = {
        'altitude': {'key': 'altitude', 'type': 'float'},
        'latitude': {'key': 'latitude', 'type': 'float'},
        'longitude': {'key': 'longitude', 'type': 'float'},
    }

    def __init__(self, altitude=None, latitude=None, longitude=None):
        super(MicrosoftgraphgeoCoordinates, self).__init__()
        self.altitude = altitude
        self.latitude = latitude
        self.longitude = longitude
