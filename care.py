import utilities as ut


def care_menu(self, msg):

    def care_button(div, text, click):
        b = ut.create_button(div, text, click)
        b.header = self.header
        b.player = self.player
        return b

    self.display.delete()
    self.display.snacks = care_button(
        self.display,
        "Eat Snack for 25 Stamina",
        eat_snack
    )
    self.display.snacks = care_button(
        self.display,
        "Sleep for 8 hours",
        sleep
    )
    pass


def eat_snack(self, msg):
    if self.player['Snacks'] > 0:
        self.player['Snacks'] += -1
        self.player['Stamina'] += 25
        self.header.snack_banner.label.text = f'Snacks: {self.player["Snacks"]}'
        self.header.stamina_banner.label.text = f'Stamina: {self.player["Stamina"]}'
    pass


def sleep(self, msg):
    self.player['Fatigue'] -= 8
    if self.player['Fatigue'] < -2:
        self.player['Fatigue'] = -2
    ut.update_time(480, self.header, self.player)
    ut.update_stamina_banner(-100, self.header, self.player)
    pass
