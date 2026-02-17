from otree.api import *

doc = """
Survey Player (Biodata) - Moral Environment
"""


class Constants(BaseConstants):
    name_in_url = 'survey_player'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
