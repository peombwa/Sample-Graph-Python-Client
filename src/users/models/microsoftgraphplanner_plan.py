# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphplannerPlan(Model):
    """MicrosoftgraphplannerPlan.

    :param id:
    :type id: str
    :param created_by:
    :type created_by: ~users.models.MicrosoftgraphidentitySet
    :param created_date_time:
    :type created_date_time: datetime
    :param owner:
    :type owner: str
    :param title:
    :type title: str
    :param contexts:
    :type contexts: object
    :param tasks:
    :type tasks: list[~users.models.MicrosoftgraphplannerTask]
    :param buckets:
    :type buckets: list[~users.models.MicrosoftgraphplannerBucket]
    :param details:
    :type details: ~users.models.MicrosoftgraphplannerPlanDetails
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'created_by': {'key': 'createdBy', 'type': 'MicrosoftgraphidentitySet'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'owner': {'key': 'owner', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'contexts': {'key': 'contexts', 'type': 'object'},
        'tasks': {'key': 'tasks', 'type': '[MicrosoftgraphplannerTask]'},
        'buckets': {'key': 'buckets', 'type': '[MicrosoftgraphplannerBucket]'},
        'details': {'key': 'details', 'type': 'MicrosoftgraphplannerPlanDetails'},
    }

    def __init__(self, id=None, created_by=None, created_date_time=None, owner=None, title=None, contexts=None, tasks=None, buckets=None, details=None):
        super(MicrosoftgraphplannerPlan, self).__init__()
        self.id = id
        self.created_by = created_by
        self.created_date_time = created_date_time
        self.owner = owner
        self.title = title
        self.contexts = contexts
        self.tasks = tasks
        self.buckets = buckets
        self.details = details
