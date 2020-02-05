# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphSensitivitypolicysettingsallof1(Model):
    """sensitivityPolicySettings.

    :param is_mandatory:
    :type is_mandatory: bool
    :param help_web_url:
    :type help_web_url: str
    :param downgrade_sensitivity_requires_justification:
    :type downgrade_sensitivity_requires_justification: bool
    """

    _attribute_map = {
        'is_mandatory': {'key': 'isMandatory', 'type': 'bool'},
        'help_web_url': {'key': 'helpWebUrl', 'type': 'str'},
        'downgrade_sensitivity_requires_justification': {'key': 'downgradeSensitivityRequiresJustification', 'type': 'bool'},
    }

    def __init__(self, is_mandatory=None, help_web_url=None, downgrade_sensitivity_requires_justification=None):
        super(ComponentsschemasmicrosoftGraphSensitivitypolicysettingsallof1, self).__init__()
        self.is_mandatory = is_mandatory
        self.help_web_url = help_web_url
        self.downgrade_sensitivity_requires_justification = downgrade_sensitivity_requires_justification
