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
    prospek_terpilih = models.StringField()
    angka_keluar = models.IntegerField(initial=0)
    hasil_token = models.IntegerField(initial=0)
