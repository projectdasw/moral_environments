from otree.api import *

doc = """
Ambiguity Task - Moral Environment
"""


class Constants(BaseConstants):
    name_in_url = 'ambiguity_task'
    players_per_group = None
    num_rounds = 1
    colors = ['Biru', 'Merah', 'Kuning']
    payoff_A = 150
    payoff_B = 80


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    prospek_terpilih = models.StringField()
    bola_keluar = models.StringField()
    hasil_token = models.IntegerField(initial=0)
