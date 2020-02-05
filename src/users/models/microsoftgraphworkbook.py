# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Microsoftgraphworkbook(Model):
    """Microsoftgraphworkbook.

    :param id:
    :type id: str
    :param application:
    :type application: ~users.models.MicrosoftgraphworkbookApplication
    :param names:
    :type names: list[~users.models.MicrosoftgraphworkbookNamedItem]
    :param tables:
    :type tables: list[~users.models.MicrosoftgraphworkbookTable]
    :param worksheets:
    :type worksheets: list[~users.models.MicrosoftgraphworkbookWorksheet]
    :param comments:
    :type comments: list[~users.models.MicrosoftgraphworkbookComment]
    :param functions:
    :type functions: ~users.models.MicrosoftgraphworkbookFunctions
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'application': {'key': 'application', 'type': 'MicrosoftgraphworkbookApplication'},
        'names': {'key': 'names', 'type': '[MicrosoftgraphworkbookNamedItem]'},
        'tables': {'key': 'tables', 'type': '[MicrosoftgraphworkbookTable]'},
        'worksheets': {'key': 'worksheets', 'type': '[MicrosoftgraphworkbookWorksheet]'},
        'comments': {'key': 'comments', 'type': '[MicrosoftgraphworkbookComment]'},
        'functions': {'key': 'functions', 'type': 'MicrosoftgraphworkbookFunctions'},
    }

    def __init__(self, id=None, application=None, names=None, tables=None, worksheets=None, comments=None, functions=None):
        super(Microsoftgraphworkbook, self).__init__()
        self.id = id
        self.application = application
        self.names = names
        self.tables = tables
        self.worksheets = worksheets
        self.comments = comments
        self.functions = functions
