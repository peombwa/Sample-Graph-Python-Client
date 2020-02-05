# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphvisualInfo(Model):
    """visualInfo.

    :param attribution:
    :type attribution: ~users.models.MicrosoftgraphimageInfo
    :param background_color:
    :type background_color: str
    :param description:
    :type description: str
    :param display_text:
    :type display_text: str
    :param content:
    :type content: object
    """

    _attribute_map = {
        'attribution': {'key': 'attribution', 'type': 'MicrosoftgraphimageInfo'},
        'background_color': {'key': 'backgroundColor', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'display_text': {'key': 'displayText', 'type': 'str'},
        'content': {'key': 'content', 'type': 'object'},
    }

    def __init__(self, attribution=None, background_color=None, description=None, display_text=None, content=None):
        super(MicrosoftgraphvisualInfo, self).__init__()
        self.attribution = attribution
        self.background_color = background_color
        self.description = description
        self.display_text = display_text
        self.content = content