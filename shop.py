import utilities as ut
import random
import lists

def buy_desk_item(self, msg):
    def set_qty_label(stat):
        if stat == 'Paper':
            return 'Sheets'
        if stat == 'Ink':
            return 'Milliliters'
        pass
    qty_label = set_qty_label(self.stat)
    if player['Money'] >= self.cost:
        ut.update_money_banner(self.cost, header, player)
        player['Desk'][self.stat][qty_label] += self.qty
        self.desk.delete()
        ut.update_desk_banner(self.desk, player)
    pass

def create_market_dictionary():
    return {
        'Fruit': create_fruit_list(),
        'Vegetable': create_vegetable_list(),
        'Pastry': create_pastry_list(),
        'Stocks': [],
        'Stocked?': False
    }


def create_writing_dictionary():
    return {
        'Stocks': [],
        'Stocked?': False
    }


def create_bookshop_dictionary():
    return {
        'Stocks': ut.populate_library(),
        'Stocked?': True
    }

def create_fruit_list():
    return create_food_list(lists.fruit)


def create_vegetable_list():
    return create_food_list(lists.vegetable)


def create_pastry_list():
    return create_food_list(lists.pastry_base)


def create_food_list(input_list):
    dict = {}
    for i in input_list:
        dict.update({i: random.randrange(5, 15)})
    return dict


def buy_market_item(self, msg):
    pass


def buy_food(self, msg):
    if player['Money'] >= self.dict['Price']:
        player['Stocks']['Food'].append(self.dict)
        self.stocks.remove(self.dict)
        ut.update_money_banner(self.dict['Price'], header, player)
        ut.update_food_banner(header, player)
    display_stocks(self.div, self.stocks)
    pass


def show_food_info(self, msg):
    self.display.delete()
    self.display.info = ut.text_div(
        self.display,
        (
            f'This {self.dict["Type"]} restores '
            f'{self.dict["Restore"]} '
            f'stamina and costs {self.dict["Price"]}'
        ),
        ut.base_class_dark + 'justify-center w-1/4 max-w-min bg-gray-700 '
    )
    pass

def display_stocks(div, stocks):
    div.delete()
    for i in stocks:
        div.i = ut.create_button(
            div,
            f'Buy {i["Name"]}',
            buy_food
        )
        div.i.info = ut.new_para(div.i, 'text-xs ')
        div.i.info.text = (f'Restores {i["Restore"]} for ${i["Price"]}')
        div.i.dict = i
        div.i.stocks = stocks
        div.i.div = div

def visit_market(self, msg):

    def stock_food(food_list):
        food = random.choice(food_list)
        if food_list is lists.vegetable:
            food_type = 'vegetable'
            restore = self.stocks['Vegetable'][food]
        elif food_list is lists.fruit:
            food_type = 'fruit'
            restore = self.stocks['Fruit'][food]
        else:
            food_type = 'pastry'
            restore = self.stocks['Pastry'][food]
        price = random.randrange(5, 12)

        return {
            'Name': food, 
            'Type': food_type, 
            'Restore': restore,
            'Price': price
        }

    def choose_produce():
        if random.getrandbits(1) == 1:
            return lists.vegetable
        else:
            return lists.fruit

    def restock_produce():
        self.stocks['Stocks'] = []
        for _ in range(random.randrange(4, 20)):
            self.stocks['Stocks'].append(stock_food(choose_produce()))
    
    ut.update_time(60, header, player)
    self.display.options.delete()
    market_div = ut.new_div(self.display.options)
    market_div.display = ut.new_div(market_div)
    if player['Time'].hour < 9 and self.stocks['Stocked?'] is False:
        restock_produce()
        self.stocks['Stocked?'] = True
    elif player['Time'].hour > 16 and self.stocks['Stocked?'] is True:
        self.stocks['Stocked?'] = False
    if player['Time'].hour in range(self.hours[0], self.hours[1]):    
        display_stocks(market_div, self.stocks['Stocks'])


def buy_menu(self, msg):

    def shop_button(div, text, function, stock, hours):
        b = ut.create_button(div, text, function)
        b.info = ut.new_para(b, 'text-xs ')
        b.info.text = (f'{hours[0]}:00 to {hours[1]}:00')
        b.desk = self.desk
        b.display = self.display
        b.stocks = stock
        b.hours = hours
        return b

    global header
    global player

    player = self.player
    header = self.header
    

    self.display.delete()
    self.display.market = shop_button(
        self.display,
        'Market',
        visit_market,
        self.market,
        [7, 18]
    )
    self.display.supplies = shop_button(
        self.display,
        'Writing Shop',
        visit_writing,
        self.writing,
        [8, 17]
    )
    self.display.bookshop = shop_button(
        self.display,
        'Bookshop',
        visit_bookshop,
        self.bookshop,
        [8, 17]
    )

    self.display.options = ut.new_div(self.display)
    self.display.market.options = self.display.options
    
    pass
