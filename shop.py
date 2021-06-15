import utilities as ut
import bookshop
import stationary
import market
import random

def create_market_dictionary():
    return {
        'Fruit': market.create_fruit_list(),
        'Vegetable': market.create_vegetable_list(),
        'Pastry': market.create_pastry_list(),
        'Stocks': [],
        'Stocked?': False
    }


def create_writing_dictionary():
    return {
        'Stocks': [
            {
                'Name': 'Standard Paper',
                'Units': 'stacks',
                'Price': 10,
                'Inventory': 10
            },
            {
                'Name': 'Black Ink',
                'Units': 'bottles',
                'Price': 10,
                'Inventory': 10
            }
        ],
        'Stocked?': False
    }


def create_bookshop_dictionary():
    return {
        'Stocks': ut.populate_library(),
        'Stocked?': True
    }



def buy_menu(self, msg):

    def shop_button(div, text, function, stock, hours):
        b = ut.create_button(div, text, function)
        b.info = ut.new_para(b, 'text-xs ')
        b.info.text = (f'{hours[0]}:00 to {hours[1]}:00')
        b.desk = self.desk
        b.header = self.header
        b.player = self.player
        b.display = self.display
        b.stocks = stock
        b.hours = hours
        return b
    

    self.display.delete()
    self.display.market = shop_button(
        self.display,
        'Market',
        market.visit_market,
        self.market,
        [7, 18]
    )
    self.display.supplies = shop_button(
        self.display,
        'Writing Shop',
        stationary.visit_writing,
        self.writing,
        [8, 17]
    )
    self.display.bookshop = shop_button(
        self.display,
        'Bookshop',
        bookshop.visit_bookshop,
        self.bookshop,
        [8, 17]
    )

    self.display.options = ut.new_div(self.display)
    self.display.market.options = self.display.options
    
    pass
