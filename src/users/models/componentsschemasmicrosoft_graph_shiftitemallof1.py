# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphShiftitemallof1(Model):
    """shiftItem.

    :param display_name:
    :type display_name: str
    :param notes:
    :type notes: str
    :param activities:
    :type activities: list[~users.models.MicrosoftgraphshiftActivity]
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'notes': {'key': 'notes', 'type': 'str'},
        'activities': {'key': 'activities', 'type': '[MicrosoftgraphshiftActivity]'},
    }

    def __init__(self, display_name=None, notes=None, activities=None):
        super(ComponentsschemasmicrosoftGraphShiftitemallof1, self).__init__()
        self.display_name = display_name
        self.notes = notes
        self.activities = activities
