# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphPlannerprogresstaskboardtaskformatallof1(Model):
    """plannerProgressTaskBoardTaskFormat.

    :param order_hint:
    :type order_hint: str
    """

    _attribute_map = {
        'order_hint': {'key': 'orderHint', 'type': 'str'},
    }

    def __init__(self, order_hint=None):
        super(ComponentsschemasmicrosoftGraphPlannerprogresstaskboardtaskformatallof1, self).__init__()
        self.order_hint = order_hint
