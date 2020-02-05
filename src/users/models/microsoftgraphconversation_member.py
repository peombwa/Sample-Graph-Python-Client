# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphconversationMember(Model):
    """MicrosoftgraphconversationMember.

    :param id:
    :type id: str
    :param roles:
    :type roles: list[str]
    :param display_name:
    :type display_name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'roles': {'key': 'roles', 'type': '[str]'},
        'display_name': {'key': 'displayName', 'type': 'str'},
    }

    def __init__(self, id=None, roles=None, display_name=None):
        super(MicrosoftgraphconversationMember, self).__init__()
        self.id = id
        self.roles = roles
        self.display_name = display_name
