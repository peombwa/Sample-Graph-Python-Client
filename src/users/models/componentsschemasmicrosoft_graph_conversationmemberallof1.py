# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphConversationmemberallof1(Model):
    """conversationMember.

    :param roles:
    :type roles: list[str]
    :param display_name:
    :type display_name: str
    """

    _attribute_map = {
        'roles': {'key': 'roles', 'type': '[str]'},
        'display_name': {'key': 'displayName', 'type': 'str'},
    }

    def __init__(self, roles=None, display_name=None):
        super(ComponentsschemasmicrosoftGraphConversationmemberallof1, self).__init__()
        self.roles = roles
        self.display_name = display_name