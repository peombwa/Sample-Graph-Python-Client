# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphOnenoteallof1(Model):
    """onenote.

    :param notebooks:
    :type notebooks: list[~users.models.Microsoftgraphnotebook]
    :param sections:
    :type sections: list[~users.models.MicrosoftgraphonenoteSection]
    :param section_groups:
    :type section_groups: list[~users.models.MicrosoftgraphsectionGroup]
    :param pages:
    :type pages: list[~users.models.MicrosoftgraphonenotePage]
    :param resources:
    :type resources: list[~users.models.MicrosoftgraphonenoteResource]
    :param operations:
    :type operations: list[~users.models.MicrosoftgraphonenoteOperation]
    """

    _attribute_map = {
        'notebooks': {'key': 'notebooks', 'type': '[Microsoftgraphnotebook]'},
        'sections': {'key': 'sections', 'type': '[MicrosoftgraphonenoteSection]'},
        'section_groups': {'key': 'sectionGroups', 'type': '[MicrosoftgraphsectionGroup]'},
        'pages': {'key': 'pages', 'type': '[MicrosoftgraphonenotePage]'},
        'resources': {'key': 'resources', 'type': '[MicrosoftgraphonenoteResource]'},
        'operations': {'key': 'operations', 'type': '[MicrosoftgraphonenoteOperation]'},
    }

    def __init__(self, notebooks=None, sections=None, section_groups=None, pages=None, resources=None, operations=None):
        super(ComponentsschemasmicrosoftGraphOnenoteallof1, self).__init__()
        self.notebooks = notebooks
        self.sections = sections
        self.section_groups = section_groups
        self.pages = pages
        self.resources = resources
        self.operations = operations