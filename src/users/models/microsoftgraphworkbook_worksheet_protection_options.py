# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphworkbookWorksheetProtectionOptions(Model):
    """workbookWorksheetProtectionOptions.

    :param allow_auto_filter:
    :type allow_auto_filter: bool
    :param allow_delete_columns:
    :type allow_delete_columns: bool
    :param allow_delete_rows:
    :type allow_delete_rows: bool
    :param allow_format_cells:
    :type allow_format_cells: bool
    :param allow_format_columns:
    :type allow_format_columns: bool
    :param allow_format_rows:
    :type allow_format_rows: bool
    :param allow_insert_columns:
    :type allow_insert_columns: bool
    :param allow_insert_hyperlinks:
    :type allow_insert_hyperlinks: bool
    :param allow_insert_rows:
    :type allow_insert_rows: bool
    :param allow_pivot_tables:
    :type allow_pivot_tables: bool
    :param allow_sort:
    :type allow_sort: bool
    """

    _attribute_map = {
        'allow_auto_filter': {'key': 'allowAutoFilter', 'type': 'bool'},
        'allow_delete_columns': {'key': 'allowDeleteColumns', 'type': 'bool'},
        'allow_delete_rows': {'key': 'allowDeleteRows', 'type': 'bool'},
        'allow_format_cells': {'key': 'allowFormatCells', 'type': 'bool'},
        'allow_format_columns': {'key': 'allowFormatColumns', 'type': 'bool'},
        'allow_format_rows': {'key': 'allowFormatRows', 'type': 'bool'},
        'allow_insert_columns': {'key': 'allowInsertColumns', 'type': 'bool'},
        'allow_insert_hyperlinks': {'key': 'allowInsertHyperlinks', 'type': 'bool'},
        'allow_insert_rows': {'key': 'allowInsertRows', 'type': 'bool'},
        'allow_pivot_tables': {'key': 'allowPivotTables', 'type': 'bool'},
        'allow_sort': {'key': 'allowSort', 'type': 'bool'},
    }

    def __init__(self, allow_auto_filter=None, allow_delete_columns=None, allow_delete_rows=None, allow_format_cells=None, allow_format_columns=None, allow_format_rows=None, allow_insert_columns=None, allow_insert_hyperlinks=None, allow_insert_rows=None, allow_pivot_tables=None, allow_sort=None):
        super(MicrosoftgraphworkbookWorksheetProtectionOptions, self).__init__()
        self.allow_auto_filter = allow_auto_filter
        self.allow_delete_columns = allow_delete_columns
        self.allow_delete_rows = allow_delete_rows
        self.allow_format_cells = allow_format_cells
        self.allow_format_columns = allow_format_columns
        self.allow_format_rows = allow_format_rows
        self.allow_insert_columns = allow_insert_columns
        self.allow_insert_hyperlinks = allow_insert_hyperlinks
        self.allow_insert_rows = allow_insert_rows
        self.allow_pivot_tables = allow_pivot_tables
        self.allow_sort = allow_sort
