# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphChatthreadallof1(Model):
    """chatThread.

    :param root_message:
    :type root_message: ~users.models.MicrosoftgraphchatMessage
    """

    _attribute_map = {
        'root_message': {'key': 'rootMessage', 'type': 'MicrosoftgraphchatMessage'},
    }

    def __init__(self, root_message=None):
        super(ComponentsschemasmicrosoftGraphChatthreadallof1, self).__init__()
        self.root_message = root_message
