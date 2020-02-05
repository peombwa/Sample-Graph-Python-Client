# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphPersonnameallof1(Model):
    """personName.

    :param display_name:
    :type display_name: str
    :param first:
    :type first: str
    :param initials:
    :type initials: str
    :param last:
    :type last: str
    :param language_tag:
    :type language_tag: str
    :param maiden:
    :type maiden: str
    :param middle:
    :type middle: str
    :param nickname:
    :type nickname: str
    :param suffix:
    :type suffix: str
    :param title:
    :type title: str
    :param pronunciation:
    :type pronunciation: ~users.models.MicrosoftgraphyomiPersonName
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'first': {'key': 'first', 'type': 'str'},
        'initials': {'key': 'initials', 'type': 'str'},
        'last': {'key': 'last', 'type': 'str'},
        'language_tag': {'key': 'languageTag', 'type': 'str'},
        'maiden': {'key': 'maiden', 'type': 'str'},
        'middle': {'key': 'middle', 'type': 'str'},
        'nickname': {'key': 'nickname', 'type': 'str'},
        'suffix': {'key': 'suffix', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'pronunciation': {'key': 'pronunciation', 'type': 'MicrosoftgraphyomiPersonName'},
    }

    def __init__(self, display_name=None, first=None, initials=None, last=None, language_tag=None, maiden=None, middle=None, nickname=None, suffix=None, title=None, pronunciation=None):
        super(ComponentsschemasmicrosoftGraphPersonnameallof1, self).__init__()
        self.display_name = display_name
        self.first = first
        self.initials = initials
        self.last = last
        self.language_tag = language_tag
        self.maiden = maiden
        self.middle = middle
        self.nickname = nickname
        self.suffix = suffix
        self.title = title
        self.pronunciation = pronunciation