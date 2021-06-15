import utilities as ut 
import random

def buy_book(self, msg):
    if player['Money'] >= self.dict['Base Price']:
        player['Library'].append(self.dict)
        self.stocks.remove(self.dict)
        ut.update_money_banner(self.dict['Base Price'], header, player)
    display_books(self.div, self.stocks)


def display_books(div, stocks):
    div.delete()
    for i in stocks:
        div.i = ut.create_buy_button(
            div,
            f'Buy {i["Title"]}',
            buy_book,
            i,
            stocks,
            (   
                f'A {ut.book_type(i["Word Count"])} '
                f'By {i["Author"]}: '
                f'${i["Base Price"]}'
            )
        )


def visit_bookshop(self, msg):
    
    def restock_books():
        for _ in random.randrange(10):
            self.stocks['Stocks'].append(ut.new_book())

    market_div = ut.d
    ut.update_time(30, header, player)
    self.display.options.delete()
    market_div = ut.new_div(self.display.options)
    market_div.display = ut.new_div(market_div)
    if player['Time'].hour < 5 and self.stocks['Stocked?'] is False:
        restock_books()
        self.stocks['Stocked?'] = True
    elif player['Time'].hour > 16 and self.stocks['Stocked?'] is True:
        self.stocks['Stocked?'] = False
    if player['Time'].hour in range(self.hours[0], self.hours[1]):    
        display_books(market_div, self.stocks['Stocks'])

