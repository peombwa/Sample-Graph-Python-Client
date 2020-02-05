# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphcolumnDefinition(Model):
    """MicrosoftgraphcolumnDefinition.

    :param id:
    :type id: str
    :param boolean:
    :type boolean: object
    :param calculated:
    :type calculated: ~users.models.MicrosoftgraphcalculatedColumn
    :param choice:
    :type choice: ~users.models.MicrosoftgraphchoiceColumn
    :param column_group:
    :type column_group: str
    :param currency:
    :type currency: ~users.models.MicrosoftgraphcurrencyColumn
    :param date_time_property:
    :type date_time_property: ~users.models.MicrosoftgraphdateTimeColumn
    :param default_value:
    :type default_value: ~users.models.MicrosoftgraphdefaultColumnValue
    :param description:
    :type description: str
    :param display_name:
    :type display_name: str
    :param enforce_unique_values:
    :type enforce_unique_values: bool
    :param geolocation:
    :type geolocation: object
    :param hidden:
    :type hidden: bool
    :param indexed:
    :type indexed: bool
    :param lookup:
    :type lookup: ~users.models.MicrosoftgraphlookupColumn
    :param name:
    :type name: str
    :param number:
    :type number: ~users.models.MicrosoftgraphnumberColumn
    :param person_or_group:
    :type person_or_group: ~users.models.MicrosoftgraphpersonOrGroupColumn
    :param read_only:
    :type read_only: bool
    :param required:
    :type required: bool
    :param text:
    :type text: ~users.models.MicrosoftgraphtextColumn
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'boolean': {'key': 'boolean', 'type': 'object'},
        'calculated': {'key': 'calculated', 'type': 'MicrosoftgraphcalculatedColumn'},
        'choice': {'key': 'choice', 'type': 'MicrosoftgraphchoiceColumn'},
        'column_group': {'key': 'columnGroup', 'type': 'str'},
        'currency': {'key': 'currency', 'type': 'MicrosoftgraphcurrencyColumn'},
        'date_time_property': {'key': 'dateTime', 'type': 'MicrosoftgraphdateTimeColumn'},
        'default_value': {'key': 'defaultValue', 'type': 'MicrosoftgraphdefaultColumnValue'},
        'description': {'key': 'description', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'enforce_unique_values': {'key': 'enforceUniqueValues', 'type': 'bool'},
        'geolocation': {'key': 'geolocation', 'type': 'object'},
        'hidden': {'key': 'hidden', 'type': 'bool'},
        'indexed': {'key': 'indexed', 'type': 'bool'},
        'lookup': {'key': 'lookup', 'type': 'MicrosoftgraphlookupColumn'},
        'name': {'key': 'name', 'type': 'str'},
        'number': {'key': 'number', 'type': 'MicrosoftgraphnumberColumn'},
        'person_or_group': {'key': 'personOrGroup', 'type': 'MicrosoftgraphpersonOrGroupColumn'},
        'read_only': {'key': 'readOnly', 'type': 'bool'},
        'required': {'key': 'required', 'type': 'bool'},
        'text': {'key': 'text', 'type': 'MicrosoftgraphtextColumn'},
    }

    def __init__(self, id=None, boolean=None, calculated=None, choice=None, column_group=None, currency=None, date_time_property=None, default_value=None, description=None, display_name=None, enforce_unique_values=None, geolocation=None, hidden=None, indexed=None, lookup=None, name=None, number=None, person_or_group=None, read_only=None, required=None, text=None):
        super(MicrosoftgraphcolumnDefinition, self).__init__()
        self.id = id
        self.boolean = boolean
        self.calculated = calculated
        self.choice = choice
        self.column_group = column_group
        self.currency = currency
        self.date_time_property = date_time_property
        self.default_value = default_value
        self.description = description
        self.display_name = display_name
        self.enforce_unique_values = enforce_unique_values
        self.geolocation = geolocation
        self.hidden = hidden
        self.indexed = indexed
        self.lookup = lookup
        self.name = name
        self.number = number
        self.person_or_group = person_or_group
        self.read_only = read_only
        self.required = required
        self.text = text
