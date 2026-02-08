from otree.api import *

doc = """
Risk Task - Moral Environment
"""


class Constants(BaseConstants):
    name_in_url = 'risk_task'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
