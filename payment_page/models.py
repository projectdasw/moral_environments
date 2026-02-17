from otree.api import *

doc = """
Payment Page - Moral Environment
"""


class Constants(BaseConstants):
    name_in_url = 'payment_page'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    chosen_app = models.StringField(blank=True)
