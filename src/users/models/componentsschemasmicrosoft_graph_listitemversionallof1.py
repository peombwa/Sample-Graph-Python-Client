# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphListitemversionallof1(Model):
    """listItemVersion.

    :param fields:
    :type fields: ~users.models.MicrosoftgraphfieldValueSet
    """

    _attribute_map = {
        'fields': {'key': 'fields', 'type': 'MicrosoftgraphfieldValueSet'},
    }

    def __init__(self, fields=None):
        super(ComponentsschemasmicrosoftGraphListitemversionallof1, self).__init__()
        self.fields = fields
