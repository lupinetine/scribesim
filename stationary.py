import utilities as ut 
import random

def visit_writing(self, msg):

    def restock_stationary():
        for i in self.stocks['Stocks']:
            i['Inventory'] += random.randrange(10)
    self.div = ut.store_div(self)
    ut.stock_shelves(self, restock_stationary)
    ut.store_display(self, display_writing)
    

def display_writing(div, self):
    div.delete()
    for i in self.stocks['Stocks']:
        div.i = ut.create_buy_button(
            div,
            f'Buy {i["Name"]}',
            buy_desk_item,
            i,
            self.stocks,
            (
                f'{i["Inventory"]} {i["Units"]} '
                f'in stock : ${i["Price"]} each'
            )
        )
        div.i.desk = self.desk
        div.i.player = self.player
        div.i.header = self.header

def buy_desk_item(self, msg):
    print('miao')
    if self.player['Money'] >= self.dict['Price']:
        if self.dict['Name'] == 'Standard Paper':
            self.player['Desk']['Paper']['Sheets'] += 100
            self.stocks['Stocks'][0]['Inventory'] -= 1
            ut.update_money_banner(self.dict['Price'], self.header, self.player)
        elif self.dict['Name'] == 'Black Ink':
            self.player['Desk']['Ink']['Milliliters'] += 50
            self.stocks['Stocks'][1]['Inventory'] -= 1
            ut.update_money_banner(self.dict['Price'], self.header, self.player)
        else:
            return
    self.desk.delete()
    ut.update_desk_banner(self.desk, self.player)
    display_writing(self.div, self)
    pass
