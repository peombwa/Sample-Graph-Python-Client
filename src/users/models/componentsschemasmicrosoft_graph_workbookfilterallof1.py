# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphWorkbookfilterallof1(Model):
    """workbookFilter.

    :param criteria:
    :type criteria: ~users.models.MicrosoftgraphworkbookFilterCriteria
    """

    _attribute_map = {
        'criteria': {'key': 'criteria', 'type': 'MicrosoftgraphworkbookFilterCriteria'},
    }

    def __init__(self, criteria=None):
        super(ComponentsschemasmicrosoftGraphWorkbookfilterallof1, self).__init__()
        self.criteria = criteria
