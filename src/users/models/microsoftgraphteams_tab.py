# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphteamsTab(Model):
    """MicrosoftgraphteamsTab.

    :param id:
    :type id: str
    :param name:
    :type name: str
    :param display_name:
    :type display_name: str
    :param teams_app_id:
    :type teams_app_id: str
    :param sort_order_index:
    :type sort_order_index: str
    :param message_id:
    :type message_id: str
    :param web_url:
    :type web_url: str
    :param configuration:
    :type configuration: ~users.models.MicrosoftgraphteamsTabConfiguration
    :param teams_app:
    :type teams_app: ~users.models.MicrosoftgraphteamsApp
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'teams_app_id': {'key': 'teamsAppId', 'type': 'str'},
        'sort_order_index': {'key': 'sortOrderIndex', 'type': 'str'},
        'message_id': {'key': 'messageId', 'type': 'str'},
        'web_url': {'key': 'webUrl', 'type': 'str'},
        'configuration': {'key': 'configuration', 'type': 'MicrosoftgraphteamsTabConfiguration'},
        'teams_app': {'key': 'teamsApp', 'type': 'MicrosoftgraphteamsApp'},
    }

    def __init__(self, id=None, name=None, display_name=None, teams_app_id=None, sort_order_index=None, message_id=None, web_url=None, configuration=None, teams_app=None):
        super(MicrosoftgraphteamsTab, self).__init__()
        self.id = id
        self.name = name
        self.display_name = display_name
        self.teams_app_id = teams_app_id
        self.sort_order_index = sort_order_index
        self.message_id = message_id
        self.web_url = web_url
        self.configuration = configuration
        self.teams_app = teams_app
