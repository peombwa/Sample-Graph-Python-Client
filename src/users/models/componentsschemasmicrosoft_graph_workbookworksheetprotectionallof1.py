# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphWorkbookworksheetprotectionallof1(Model):
    """workbookWorksheetProtection.

    :param options:
    :type options:
     ~users.models.MicrosoftgraphworkbookWorksheetProtectionOptions
    :param protected:
    :type protected: bool
    """

    _attribute_map = {
        'options': {'key': 'options', 'type': 'MicrosoftgraphworkbookWorksheetProtectionOptions'},
        'protected': {'key': 'protected', 'type': 'bool'},
    }

    def __init__(self, options=None, protected=None):
        super(ComponentsschemasmicrosoftGraphWorkbookworksheetprotectionallof1, self).__init__()
        self.options = options
        self.protected = protected
