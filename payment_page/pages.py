from .models import *
import random


class info_all_round(Page):
    def vars_for_template(self):
        # Uang kehadiran (ambil dari session config)
        show_up_fee = self.session.config.get('participation_fee', 0)

        # RISK TASK
        risk_players = []

        for p in self.participant.get_players():
            if p.__module__.startswith('risk_task'):
                risk_players.append(p)

        risk_data = []
        total_risk = 0

        for p in risk_players:
            risk_data.append({
                'round_number': p.round_number,
                'choice': 'Prospek A' if p.prospek_terpilih == 'prospek-A' else 'Prospek B',
                'payoff': p.hasil_token,
            })

            total_risk += p.hasil_token

        # AMBIGUITY TASK
        ambiguity_players = []

        for p in self.participant.get_players():
            if p.__module__.startswith('ambiguity_task'):
                ambiguity_players.append(p)

        ambiguity_data = []
        total_ambiguity = 0

        for p in ambiguity_players:
            ambiguity_data.append({
                'round_number': p.round_number,
                'choice':
                    'Prospek A (Bola Biru)' if p.prospek_terpilih == 'prospek-A' else 'Prospek B (Bola Merah/Kuning)',
                'drawn_color': p.bola_keluar,
                'payoff': p.hasil_token,
            })

            total_ambiguity += p.hasil_token

        return dict(
            ambiguity_data=sorted(ambiguity_data, key=lambda x: x['round_number']),
            risk_data=sorted(risk_data, key=lambda x: x['round_number']),
            total_ambiguity=total_ambiguity,
            total_risk=total_risk,
            show_up_fee=show_up_fee,
            # final_payment=final_payment
        )

        # COMPANY TASK


class get_payment(Page):
    def vars_for_template(self):
        allowed_apps = ["risk_task", "ambiguity_task", "company_task"]
        if not self.player.field_maybe_none('chosen_app'):  # cek field model, bukan participant.vars
            app_list = []

            for p in self.player.participant.get_players():
                app_name = p.__class__.__module__.split('.')[0]

                if app_name in allowed_apps:
                    app_list.append(app_name)

            chosen_app = random.choice(app_list)

            # simpan ke database
            self.player.chosen_app = chosen_app

        return dict(
            chosen_app=self.player.chosen_app
        )


class result(Page):
    pass


page_sequence = [
    info_all_round,
    get_payment,
    result
]