# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphUserteamworkallof1(Model):
    """userTeamwork.

    :param installed_apps:
    :type installed_apps:
     list[~users.models.MicrosoftgraphteamsAppInstallation]
    """

    _attribute_map = {
        'installed_apps': {'key': 'installedApps', 'type': '[MicrosoftgraphteamsAppInstallation]'},
    }

    def __init__(self, installed_apps=None):
        super(ComponentsschemasmicrosoftGraphUserteamworkallof1, self).__init__()
        self.installed_apps = installed_apps
