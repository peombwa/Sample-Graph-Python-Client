# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphplannerCategoryDescriptions(Model):
    """plannerCategoryDescriptions.

    :param category1:
    :type category1: str
    :param category2:
    :type category2: str
    :param category3:
    :type category3: str
    :param category4:
    :type category4: str
    :param category5:
    :type category5: str
    :param category6:
    :type category6: str
    """

    _attribute_map = {
        'category1': {'key': 'category1', 'type': 'str'},
        'category2': {'key': 'category2', 'type': 'str'},
        'category3': {'key': 'category3', 'type': 'str'},
        'category4': {'key': 'category4', 'type': 'str'},
        'category5': {'key': 'category5', 'type': 'str'},
        'category6': {'key': 'category6', 'type': 'str'},
    }

    def __init__(self, category1=None, category2=None, category3=None, category4=None, category5=None, category6=None):
        super(MicrosoftgraphplannerCategoryDescriptions, self).__init__()
        self.category1 = category1
        self.category2 = category2
        self.category3 = category3
        self.category4 = category4
        self.category5 = category5
        self.category6 = category6
