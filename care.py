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
    pass

def eat_snack(self, msg):
    if self.player['Snacks'] > 0:
        self.player['Snacks'] += -1
        self.player['Stamina'] += 25
        self.header.snack_banner.label.text = f'Snacks: {self.player["Snacks"]}'
        self.header.stamina_banner.label.text = f'Stamina: {self.player["Stamina"]}'
    pass
