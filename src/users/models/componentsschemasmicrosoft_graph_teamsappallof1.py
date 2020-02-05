# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphTeamsappallof1(Model):
    """teamsApp.

    :param external_id:
    :type external_id: str
    :param name:
    :type name: str
    :param display_name:
    :type display_name: str
    :param distribution_method: Possible values include: 'store',
     'organization', 'sideloaded', 'unknownFutureValue'
    :type distribution_method: str or ~users.models.enum
    :param app_definitions:
    :type app_definitions:
     list[~users.models.MicrosoftgraphteamsAppDefinition]
    """

    _attribute_map = {
        'external_id': {'key': 'externalId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'distribution_method': {'key': 'distributionMethod', 'type': 'str'},
        'app_definitions': {'key': 'appDefinitions', 'type': '[MicrosoftgraphteamsAppDefinition]'},
    }

    def __init__(self, external_id=None, name=None, display_name=None, distribution_method=None, app_definitions=None):
        super(ComponentsschemasmicrosoftGraphTeamsappallof1, self).__init__()
        self.external_id = external_id
        self.name = name
        self.display_name = display_name
        self.distribution_method = distribution_method
        self.app_definitions = app_definitions