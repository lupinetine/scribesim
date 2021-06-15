import utilities as ut 
import random

def buy_book(self, msg):
    if self.player['Money'] >= self.dict['Base Price']:
        self.player['Library'].append(self.dict)
        self.stocks.remove(self.dict)
        ut.update_money_banner(self.dict['Base Price'], self.header, self.player)
    display_books(self.div, self.stocks)


def display_books(div, self):
    div.delete()
    for i in self.stocks['Stocks']:
        div.i = ut.create_buy_button(
            div,
            f'Buy {i["Title"]}',
            buy_book,
            i,
            self.stocks,
            (   
                f'A {ut.book_type(i["Word Count"])} '
                f'By {i["Author"]}: '
                f'${i["Base Price"]}'
            )
        )
        div.i.player = self.player
        div.i.header = self.header

def visit_bookshop(self, msg):
    
    def restock_books():
        for _ in random.randrange(10):
            self.stocks['Stocks'].append(ut.new_book())

    
    self.div = ut.store_div(self)
    ut.stock_shelves(self, restock_books)
    ut.store_display(self, display_books)

