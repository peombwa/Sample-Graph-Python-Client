# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Microsoftgraphprofile(Model):
    """Microsoftgraphprofile.

    :param id:
    :type id: str
    :param account:
    :type account: list[~users.models.MicrosoftgraphuserAccountInformation]
    :param anniversaries:
    :type anniversaries: list[~users.models.MicrosoftgraphpersonAnniversary]
    :param educational_activities:
    :type educational_activities:
     list[~users.models.MicrosoftgrapheducationalActivity]
    :param emails:
    :type emails: list[~users.models.MicrosoftgraphitemEmail]
    :param interests:
    :type interests: list[~users.models.MicrosoftgraphpersonInterest]
    :param languages:
    :type languages: list[~users.models.MicrosoftgraphlanguageProficiency]
    :param names:
    :type names: list[~users.models.MicrosoftgraphpersonName]
    :param phones:
    :type phones: list[~users.models.MicrosoftgraphitemPhone]
    :param positions:
    :type positions: list[~users.models.MicrosoftgraphworkPosition]
    :param projects:
    :type projects: list[~users.models.MicrosoftgraphprojectParticipation]
    :param skills:
    :type skills: list[~users.models.MicrosoftgraphskillProficiency]
    :param web_accounts:
    :type web_accounts: list[~users.models.MicrosoftgraphwebAccount]
    :param websites:
    :type websites: list[~users.models.MicrosoftgraphpersonWebsite]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'account': {'key': 'account', 'type': '[MicrosoftgraphuserAccountInformation]'},
        'anniversaries': {'key': 'anniversaries', 'type': '[MicrosoftgraphpersonAnniversary]'},
        'educational_activities': {'key': 'educationalActivities', 'type': '[MicrosoftgrapheducationalActivity]'},
        'emails': {'key': 'emails', 'type': '[MicrosoftgraphitemEmail]'},
        'interests': {'key': 'interests', 'type': '[MicrosoftgraphpersonInterest]'},
        'languages': {'key': 'languages', 'type': '[MicrosoftgraphlanguageProficiency]'},
        'names': {'key': 'names', 'type': '[MicrosoftgraphpersonName]'},
        'phones': {'key': 'phones', 'type': '[MicrosoftgraphitemPhone]'},
        'positions': {'key': 'positions', 'type': '[MicrosoftgraphworkPosition]'},
        'projects': {'key': 'projects', 'type': '[MicrosoftgraphprojectParticipation]'},
        'skills': {'key': 'skills', 'type': '[MicrosoftgraphskillProficiency]'},
        'web_accounts': {'key': 'webAccounts', 'type': '[MicrosoftgraphwebAccount]'},
        'websites': {'key': 'websites', 'type': '[MicrosoftgraphpersonWebsite]'},
    }

    def __init__(self, id=None, account=None, anniversaries=None, educational_activities=None, emails=None, interests=None, languages=None, names=None, phones=None, positions=None, projects=None, skills=None, web_accounts=None, websites=None):
        super(Microsoftgraphprofile, self).__init__()
        self.id = id
        self.account = account
        self.anniversaries = anniversaries
        self.educational_activities = educational_activities
        self.emails = emails
        self.interests = interests
        self.languages = languages
        self.names = names
        self.phones = phones
        self.positions = positions
        self.projects = projects
        self.skills = skills
        self.web_accounts = web_accounts
        self.websites = websites