# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphPlannerassignedtotaskboardtaskformatallof1(Model):
    """plannerAssignedToTaskBoardTaskFormat.

    :param unassigned_order_hint:
    :type unassigned_order_hint: str
    :param order_hints_by_assignee:
    :type order_hints_by_assignee: object
    """

    _attribute_map = {
        'unassigned_order_hint': {'key': 'unassignedOrderHint', 'type': 'str'},
        'order_hints_by_assignee': {'key': 'orderHintsByAssignee', 'type': 'object'},
    }

    def __init__(self, unassigned_order_hint=None, order_hints_by_assignee=None):
        super(ComponentsschemasmicrosoftGraphPlannerassignedtotaskboardtaskformatallof1, self).__init__()
        self.unassigned_order_hint = unassigned_order_hint
        self.order_hints_by_assignee = order_hints_by_assignee