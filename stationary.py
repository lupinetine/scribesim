import utilities as ut 
import random

def visit_writing(self, msg):

    def restock_stationary():
        for i in self.stocks['Stocks']:
            i['Inventory'] += random.randrange(10)

    
    market_div = ut.store_display(self, restock_stationary, display_writing)


def display_writing(div, self):
    div.delete()
    for i in self.stocks['Stocks']:
        div.i = ut.create_buy_button(
            div,
            f'Buy {i["Name"]}',
            buy_desk_item,
            i,
            self.stocks['Stocks'],
            (
                f'{i["Inventory"]} {i["Units"]} '
                f'in stock : ${i["Price"]} each'
            )
        )
        div.i.desk = self.desk


def buy_desk_item(self, msg):
    if self.player['Money'] >= self.dict['Price']:
        if self.dict['Name'] == 'Standard Paper':
            self.player['Desk']['Paper']['Sheets'] += 100
            self.stocks[0]['Inventory'] -= 1
            ut.update_money_banner(self.dict['Price'], self.header, self.player)
        elif self.dict['Name'] == 'Black Ink':
            self.player['Desk']['Ink']['Milliliters'] += 50
            self.stocks[1]['Inventory'] -= 1
            ut.update_money_banner(self.dict['Price'], self.header, self.player)
        else:
            return
    self.desk.delete()
    ut.update_desk_banner(self.desk, self.player)
    display_writing(self.div, self)
    pass
