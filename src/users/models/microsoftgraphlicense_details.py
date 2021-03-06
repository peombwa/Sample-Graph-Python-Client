# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphlicenseDetails(Model):
    """MicrosoftgraphlicenseDetails.

    :param id:
    :type id: str
    :param service_plans:
    :type service_plans: list[~users.models.MicrosoftgraphservicePlanInfo]
    :param sku_id:
    :type sku_id: str
    :param sku_part_number:
    :type sku_part_number: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'service_plans': {'key': 'servicePlans', 'type': '[MicrosoftgraphservicePlanInfo]'},
        'sku_id': {'key': 'skuId', 'type': 'str'},
        'sku_part_number': {'key': 'skuPartNumber', 'type': 'str'},
    }

    def __init__(self, id=None, service_plans=None, sku_id=None, sku_part_number=None):
        super(MicrosoftgraphlicenseDetails, self).__init__()
        self.id = id
        self.service_plans = service_plans
        self.sku_id = sku_id
        self.sku_part_number = sku_part_number
