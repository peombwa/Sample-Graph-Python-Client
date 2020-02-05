# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftgraphplannerUser(Model):
    """MicrosoftgraphplannerUser.

    :param id:
    :type id: str
    :param favorite_plan_references:
    :type favorite_plan_references: object
    :param recent_plan_references:
    :type recent_plan_references: object
    :param tasks:
    :type tasks: list[~users.models.MicrosoftgraphplannerTask]
    :param plans:
    :type plans: list[~users.models.MicrosoftgraphplannerPlan]
    :param favorite_plans:
    :type favorite_plans: list[~users.models.MicrosoftgraphplannerPlan]
    :param recent_plans:
    :type recent_plans: list[~users.models.MicrosoftgraphplannerPlan]
    :param all:
    :type all: list[~users.models.MicrosoftgraphplannerDelta]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'favorite_plan_references': {'key': 'favoritePlanReferences', 'type': 'object'},
        'recent_plan_references': {'key': 'recentPlanReferences', 'type': 'object'},
        'tasks': {'key': 'tasks', 'type': '[MicrosoftgraphplannerTask]'},
        'plans': {'key': 'plans', 'type': '[MicrosoftgraphplannerPlan]'},
        'favorite_plans': {'key': 'favoritePlans', 'type': '[MicrosoftgraphplannerPlan]'},
        'recent_plans': {'key': 'recentPlans', 'type': '[MicrosoftgraphplannerPlan]'},
        'all': {'key': 'all', 'type': '[MicrosoftgraphplannerDelta]'},
    }

    def __init__(self, id=None, favorite_plan_references=None, recent_plan_references=None, tasks=None, plans=None, favorite_plans=None, recent_plans=None, all=None):
        super(MicrosoftgraphplannerUser, self).__init__()
        self.id = id
        self.favorite_plan_references = favorite_plan_references
        self.recent_plan_references = recent_plan_references
        self.tasks = tasks
        self.plans = plans
        self.favorite_plans = favorite_plans
        self.recent_plans = recent_plans
        self.all = all
