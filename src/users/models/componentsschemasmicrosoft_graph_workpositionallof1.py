# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphWorkpositionallof1(Model):
    """workPosition.

    :param categories:
    :type categories: list[str]
    :param detail:
    :type detail: ~users.models.MicrosoftgraphpositionDetail
    """

    _attribute_map = {
        'categories': {'key': 'categories', 'type': '[str]'},
        'detail': {'key': 'detail', 'type': 'MicrosoftgraphpositionDetail'},
    }

    def __init__(self, categories=None, detail=None):
        super(ComponentsschemasmicrosoftGraphWorkpositionallof1, self).__init__()
        self.categories = categories
        self.detail = detail