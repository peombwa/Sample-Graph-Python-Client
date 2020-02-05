# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Microsoftgraphchat(Model):
    """Microsoftgraphchat.

    :param id:
    :type id: str
    :param topic:
    :type topic: str
    :param created_date_time:
    :type created_date_time: datetime
    :param last_updated_date_time:
    :type last_updated_date_time: datetime
    :param installed_apps:
    :type installed_apps:
     list[~users.models.MicrosoftgraphteamsAppInstallation]
    :param members:
    :type members: list[~users.models.MicrosoftgraphconversationMember]
    :param messages:
    :type messages: list[~users.models.MicrosoftgraphchatMessage]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'topic': {'key': 'topic', 'type': 'str'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'last_updated_date_time': {'key': 'lastUpdatedDateTime', 'type': 'iso-8601'},
        'installed_apps': {'key': 'installedApps', 'type': '[MicrosoftgraphteamsAppInstallation]'},
        'members': {'key': 'members', 'type': '[MicrosoftgraphconversationMember]'},
        'messages': {'key': 'messages', 'type': '[MicrosoftgraphchatMessage]'},
    }

    def __init__(self, id=None, topic=None, created_date_time=None, last_updated_date_time=None, installed_apps=None, members=None, messages=None):
        super(Microsoftgraphchat, self).__init__()
        self.id = id
        self.topic = topic
        self.created_date_time = created_date_time
        self.last_updated_date_time = last_updated_date_time
        self.installed_apps = installed_apps
        self.members = members
        self.messages = messages