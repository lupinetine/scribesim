import utilities as ut
def buy_snack(self, msg):
    if player['Money'] >= self.cost:
        player[self.stat] += self.qty
        player['Money'] -= self.cost
        header.snack_banner.label.text = f'{self.stat}: {player[self.stat]}'
        header.money_banner.label.text = f'{"Money"}: {player["Money"]}'
    pass


def buy_desk_item(self, msg):
    def set_qty_label(stat):
        if stat == 'Paper':
            return 'Sheets'
        if stat == 'Ink':
            return 'Milliliters'
        pass
    qty_label = set_qty_label(self.stat)
    if player['Money'] >= self.cost:
        player['Desk'][self.stat][qty_label] += self.qty
        player['Money'] -= self.cost
        header.money_banner.label.text = f'{"Money"}: {player["Money"]}'
        for i in self.desk.components:
            if qty_label in i.text:
                i.text = f'{qty_label}: {player["Desk"][self.stat][qty_label]}'
    pass


def buy_menu(self, msg):

    def buy_menu_button_maker(div, text, function, stat, cost, qty, desk=None):
        button = ut.create_button(div, text, function)
        button.stat = stat
        button.cost = cost
        button.qty = qty
        button.desk = desk
        return button

    global header
    global player
    
    player = self.player
    header = self.header

    self.display.delete()
    self.display.buy_snacks = buy_menu_button_maker(
        self.display,
        "Buy Snacks @ $5/each",
        buy_snack,
        "Snacks",
        5,
        1
    )
    self.display.buy_paper = buy_menu_button_maker(
        self.display,
        "Buy Paper @ $10/100 sheets",
        buy_desk_item,
        "Paper",
        10,
        100,
        self.desk.paper
    )
    self.display.buy_ink = buy_menu_button_maker(
        self.display,
        "Buy Ink @ $5/50ml",
        buy_desk_item,
        "Ink",
        5,
        50,
        self.desk.ink
    )
    pass
