# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphSwapshiftschangerequestallof1(Model):
    """swapShiftsChangeRequest.

    :param recipient_shift_id:
    :type recipient_shift_id: str
    """

    _attribute_map = {
        'recipient_shift_id': {'key': 'recipientShiftId', 'type': 'str'},
    }

    def __init__(self, recipient_shift_id=None):
        super(ComponentsschemasmicrosoftGraphSwapshiftschangerequestallof1, self).__init__()
        self.recipient_shift_id = recipient_shift_id