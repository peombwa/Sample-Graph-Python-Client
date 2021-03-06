# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComponentsschemasmicrosoftGraphWorkbooktableallof1(Model):
    """workbookTable.

    :param highlight_first_column:
    :type highlight_first_column: bool
    :param highlight_last_column:
    :type highlight_last_column: bool
    :param legacy_id:
    :type legacy_id: str
    :param name:
    :type name: str
    :param show_banded_columns:
    :type show_banded_columns: bool
    :param show_banded_rows:
    :type show_banded_rows: bool
    :param show_filter_button:
    :type show_filter_button: bool
    :param show_headers:
    :type show_headers: bool
    :param show_totals:
    :type show_totals: bool
    :param style:
    :type style: str
    :param columns:
    :type columns: list[~users.models.MicrosoftgraphworkbookTableColumn]
    :param rows:
    :type rows: list[~users.models.MicrosoftgraphworkbookTableRow]
    :param sort:
    :type sort: ~users.models.MicrosoftgraphworkbookTableSort
    :param worksheet:
    :type worksheet: ~users.models.MicrosoftgraphworkbookWorksheet
    """

    _attribute_map = {
        'highlight_first_column': {'key': 'highlightFirstColumn', 'type': 'bool'},
        'highlight_last_column': {'key': 'highlightLastColumn', 'type': 'bool'},
        'legacy_id': {'key': 'legacyId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'show_banded_columns': {'key': 'showBandedColumns', 'type': 'bool'},
        'show_banded_rows': {'key': 'showBandedRows', 'type': 'bool'},
        'show_filter_button': {'key': 'showFilterButton', 'type': 'bool'},
        'show_headers': {'key': 'showHeaders', 'type': 'bool'},
        'show_totals': {'key': 'showTotals', 'type': 'bool'},
        'style': {'key': 'style', 'type': 'str'},
        'columns': {'key': 'columns', 'type': '[MicrosoftgraphworkbookTableColumn]'},
        'rows': {'key': 'rows', 'type': '[MicrosoftgraphworkbookTableRow]'},
        'sort': {'key': 'sort', 'type': 'MicrosoftgraphworkbookTableSort'},
        'worksheet': {'key': 'worksheet', 'type': 'MicrosoftgraphworkbookWorksheet'},
    }

    def __init__(self, highlight_first_column=None, highlight_last_column=None, legacy_id=None, name=None, show_banded_columns=None, show_banded_rows=None, show_filter_button=None, show_headers=None, show_totals=None, style=None, columns=None, rows=None, sort=None, worksheet=None):
        super(ComponentsschemasmicrosoftGraphWorkbooktableallof1, self).__init__()
        self.highlight_first_column = highlight_first_column
        self.highlight_last_column = highlight_last_column
        self.legacy_id = legacy_id
        self.name = name
        self.show_banded_columns = show_banded_columns
        self.show_banded_rows = show_banded_rows
        self.show_filter_button = show_filter_button
        self.show_headers = show_headers
        self.show_totals = show_totals
        self.style = style
        self.columns = columns
        self.rows = rows
        self.sort = sort
        self.worksheet = worksheet
