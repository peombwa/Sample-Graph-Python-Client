# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphAttendeebaseallof1(Model):
    """attendeeBase.

    :param type: Possible values include: 'required', 'optional', 'resource'
    :type type: str or ~users.models.enum
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, type=None):
        super(ComponentsschemasmicrosoftGraphAttendeebaseallof1, self).__init__()
        self.type = type
