# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphpositionDetail(Model):
    """positionDetail.

    :param company:
    :type company: ~users.models.MicrosoftgraphcompanyDetail
    :param description:
    :type description: str
    :param end_month_year:
    :type end_month_year: date
    :param job_title:
    :type job_title: str
    :param role:
    :type role: str
    :param start_month_year:
    :type start_month_year: date
    :param summary:
    :type summary: str
    """

    _attribute_map = {
        'company': {'key': 'company', 'type': 'MicrosoftgraphcompanyDetail'},
        'description': {'key': 'description', 'type': 'str'},
        'end_month_year': {'key': 'endMonthYear', 'type': 'date'},
        'job_title': {'key': 'jobTitle', 'type': 'str'},
        'role': {'key': 'role', 'type': 'str'},
        'start_month_year': {'key': 'startMonthYear', 'type': 'date'},
        'summary': {'key': 'summary', 'type': 'str'},
    }

    def __init__(self, company=None, description=None, end_month_year=None, job_title=None, role=None, start_month_year=None, summary=None):
        super(MicrosoftgraphpositionDetail, self).__init__()
        self.company = company
        self.description = description
        self.end_month_year = end_month_year
        self.job_title = job_title
        self.role = role
        self.start_month_year = start_month_year
        self.summary = summary