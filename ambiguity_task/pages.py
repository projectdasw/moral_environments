from .models import *
import random


class game(Page):
    form_model = 'player'
    form_fields = ['prospek_terpilih']

    def error_message(self, values):
        if not values.get('prospek_terpilih'):
            return "Silakan pilih salah satu prospek."

    def before_next_page(self):
        # randomisasi komposisi dengan constraint
        while True:

            blue = random.randint(10, 40)
            red = random.randint(10, 40)
            yellow = 100 - blue - red

            if 10 <= yellow <= 40:
                break

        self.player.bola_biru = blue
        self.player.bola_merah = red
        self.player.bola_kuning = yellow

        # buat list bola sesuai komposisi
        balls = (
                ['Biru'] * blue +
                ['Merah'] * red +
                ['Kuning'] * yellow
        )

        drawn = random.choice(balls)

        self.player.bola_keluar = drawn

        # payoff
        if self.player.prospek_terpilih == 'prospek-A':
            self.player.hasil_token = 150 if drawn == 'Biru' else 0

        if self.player.prospek_terpilih == 'prospek-B':
            self.player.hasil_token = 80 if drawn in ['Merah', 'Kuning'] else 0


class result(Page):
    def vars_for_template(self):
        return dict(
            choice=self.player.prospek_terpilih,
            ball=self.player.bola_keluar,
            payoff=self.player.hasil_token,
            blue=self.player.bola_biru,
            red=self.player.bola_merah,
            yellow=self.player.bola_kuning
        )


page_sequence = [
    game, result
]
