# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphfolderView(Model):
    """folderView.

    :param sort_by:
    :type sort_by: str
    :param sort_order:
    :type sort_order: str
    :param view_type:
    :type view_type: str
    """

    _attribute_map = {
        'sort_by': {'key': 'sortBy', 'type': 'str'},
        'sort_order': {'key': 'sortOrder', 'type': 'str'},
        'view_type': {'key': 'viewType', 'type': 'str'},
    }

    def __init__(self, sort_by=None, sort_order=None, view_type=None):
        super(MicrosoftgraphfolderView, self).__init__()
        self.sort_by = sort_by
        self.sort_order = sort_order
        self.view_type = view_type