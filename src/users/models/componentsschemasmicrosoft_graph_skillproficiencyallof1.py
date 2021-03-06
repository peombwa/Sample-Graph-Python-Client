# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphSkillproficiencyallof1(Model):
    """skillProficiency.

    :param categories:
    :type categories: list[str]
    :param display_name:
    :type display_name: str
    :param proficiency: Possible values include: 'elementary',
     'limitedWorking', 'generalProfessional', 'advancedProfessional', 'expert',
     'unknownFutureValue'
    :type proficiency: str or ~users.models.enum
    :param web_url:
    :type web_url: str
    """

    _attribute_map = {
        'categories': {'key': 'categories', 'type': '[str]'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'proficiency': {'key': 'proficiency', 'type': 'str'},
        'web_url': {'key': 'webUrl', 'type': 'str'},
    }

    def __init__(self, categories=None, display_name=None, proficiency=None, web_url=None):
        super(ComponentsschemasmicrosoftGraphSkillproficiencyallof1, self).__init__()
        self.categories = categories
        self.display_name = display_name
        self.proficiency = proficiency
        self.web_url = web_url
