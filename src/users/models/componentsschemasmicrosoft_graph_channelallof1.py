# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphChannelallof1(Model):
    """channel.

    :param display_name:
    :type display_name: str
    :param description:
    :type description: str
    :param is_favorite_by_default:
    :type is_favorite_by_default: bool
    :param email:
    :type email: str
    :param web_url:
    :type web_url: str
    :param membership_type: Possible values include: 'standard', 'private',
     'unknownFutureValue'
    :type membership_type: str or ~users.models.enum
    :param messages:
    :type messages: list[~users.models.MicrosoftgraphchatMessage]
    :param chat_threads:
    :type chat_threads: list[~users.models.MicrosoftgraphchatThread]
    :param tabs:
    :type tabs: list[~users.models.MicrosoftgraphteamsTab]
    :param members:
    :type members: list[~users.models.MicrosoftgraphconversationMember]
    :param files_folder:
    :type files_folder: ~users.models.MicrosoftgraphdriveItem
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'is_favorite_by_default': {'key': 'isFavoriteByDefault', 'type': 'bool'},
        'email': {'key': 'email', 'type': 'str'},
        'web_url': {'key': 'webUrl', 'type': 'str'},
        'membership_type': {'key': 'membershipType', 'type': 'str'},
        'messages': {'key': 'messages', 'type': '[MicrosoftgraphchatMessage]'},
        'chat_threads': {'key': 'chatThreads', 'type': '[MicrosoftgraphchatThread]'},
        'tabs': {'key': 'tabs', 'type': '[MicrosoftgraphteamsTab]'},
        'members': {'key': 'members', 'type': '[MicrosoftgraphconversationMember]'},
        'files_folder': {'key': 'filesFolder', 'type': 'MicrosoftgraphdriveItem'},
    }

    def __init__(self, display_name=None, description=None, is_favorite_by_default=None, email=None, web_url=None, membership_type=None, messages=None, chat_threads=None, tabs=None, members=None, files_folder=None):
        super(ComponentsschemasmicrosoftGraphChannelallof1, self).__init__()
        self.display_name = display_name
        self.description = description
        self.is_favorite_by_default = is_favorite_by_default
        self.email = email
        self.web_url = web_url
        self.membership_type = membership_type
        self.messages = messages
        self.chat_threads = chat_threads
        self.tabs = tabs
        self.members = members
        self.files_folder = files_folder
