from otree.api import *

doc = """
Ambiguity Task - Moral Environment
"""


class Constants(BaseConstants):
    name_in_url = 'ambiguity_task'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
