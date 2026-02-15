from .models import *
import random


class game(Page):
    form_model = 'player'
    form_fields = ['prospek_terpilih']

    def error_message(self, values):
        if not values.get('prospek_terpilih'):
            return "Silakan pilih salah satu prospek."

    def before_next_page(self):
        # Undian angka 1-100
        self.player.angka_keluar = random.randint(1, 100)

        if self.player.prospek_terpilih == 'prospek-A':
            if 1 <= self.player.angka_keluar <= 5:
                self.player.hasil_token = 200
            elif 6 <= self.player.angka_keluar <= 95:
                self.player.hasil_token = 150
            else:
                self.player.hasil_token = 0

        if self.player.prospek_terpilih == 'prospek-B':
            if 1 <= self.player.angka_keluar <= 5:
                self.player.hasil_token = 180
            elif 6 <= self.player.angka_keluar <= 95:
                self.player.hasil_token = 150
            else:
                self.player.hasil_token = 20

        # Set payoff oTree
        # self.player.payoff = self.player.hasil_token


class result(Page):
    pass


page_sequence = [
    game, result
]
