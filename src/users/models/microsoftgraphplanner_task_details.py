# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphplannerTaskDetails(Model):
    """MicrosoftgraphplannerTaskDetails.

    :param id:
    :type id: str
    :param description:
    :type description: str
    :param preview_type: Possible values include: 'automatic', 'noPreview',
     'checklist', 'description', 'reference'
    :type preview_type: str or ~users.models.enum
    :param references:
    :type references: object
    :param checklist:
    :type checklist: object
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'preview_type': {'key': 'previewType', 'type': 'str'},
        'references': {'key': 'references', 'type': 'object'},
        'checklist': {'key': 'checklist', 'type': 'object'},
    }

    def __init__(self, id=None, description=None, preview_type=None, references=None, checklist=None):
        super(MicrosoftgraphplannerTaskDetails, self).__init__()
        self.id = id
        self.description = description
        self.preview_type = preview_type
        self.references = references
        self.checklist = checklist
