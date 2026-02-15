from .models import *
import random


class game(Page):
    form_model = 'player'
    form_fields = ['prospek_terpilih']

    def before_next_page(self):
        # acak warna bola
        drawn_color = random.choice(Constants.colors)
        self.player.bola_keluar = drawn_color

        # tentukan payoff
        if self.player.prospek_terpilih == 'prospek-A':
            if drawn_color == 'Biru':
                self.player.hasil_token = Constants.payoff_A
            else:
                self.player.hasil_token = 0

        elif self.player.prospek_terpilih == 'prospek-B':
            if drawn_color in ['Merah', 'Kuning']:
                self.player.hasil_token = Constants.payoff_B
            else:
                self.player.hasil_token = 0


class result(Page):
    def vars_for_template(self):
        return dict(
            drawn_color=self.player.bola_keluar,
            win=self.player.hasil_token > 0
        )


page_sequence = [
    game, result
]
