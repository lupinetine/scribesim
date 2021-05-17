import utilities as ut
import random
import lists

def buy_snack(self, msg):
    if player['Money'] >= self.cost:
        ut.update_money_banner(self.cost, header, player)
        player[self.stat] += self.qty
        header.snack_banner.label.text = f'{self.stat}: {player[self.stat]}'
    pass


def create_fruit_list():
    return create_food_list(lists.fruit)

def create_vegetable_list():
    return create_food_list(lists.vegetable)

def create_food_list(input_list):
    dict = {}
    for i in input_list:
        dict.update({i: random.randrange(1, 15)})
    return dict


def buy_market_item(self, msg):
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
        ut.update_money_banner(self.cost, header, player)
        player['Desk'][self.stat][qty_label] += self.qty
        self.desk.delete()
        ut.update_desk_banner(self.desk, player)
    pass

def buy_food(self, msg):
    print('ouf')
    pass

def show_food_info(self, msg):
    self.display.delete()

    self.display.info = ut.text_div(
        self.display,
        (
            'This fruit restores '
            f'{self.stamina_restore} '
            f'stamina and costs {self.price}'
        ),
        ut.base_class_dark + 'max-w-min bg-gray-700 '
    )
    print('miao')
    pass

def visit_market(self, msg):

    def 

    def stock_food(div, type):

        if type is 'vegetable':
            food_list = lists.vegetable
            food_lookup = self.vegetable_list
        elif type is 'fruit':
            food_list = lists.fruit
            food_lookup = self.fruit_list
        else:
            food_list = lists.pastries
            food_lookup = self.pastries_list

            food = random.choice(food_list)
            price = random.randrange(5, 12)
            div.items.i = ut.create_menu_button(
                div.items, 
                f'Buy {food.title()}',
                div.display,
                buy_food
            )
            div.items.i.food = food
            div.items.i.type = type
            div.items.i.stamina_restore = food_lookup[food]
            div.items.i.price = price
            div.items.i.on('mouseenter', show_food_info)

    def restock_produce(div):
        for i in range(10):
            fruit = random.choice(lists.fruit)
            price = random.randrange(5, 12)
            div.items.i = ut.create_menu_button(
                div.items, 
                f'Buy {fruit.title()}',
                div.display,
                buy_fruit
            )
            div.items.i.food = fruit
            div.items.i.type = 'vegetable'
            div.items.i.stamina_restore = self.fruit_list[fruit]
            div.items.i.price = price
            div.items.i.on('mouseenter', show_fruit_info)
        for i in range(10):
            vegetable = random.choice(lists.vegetable)
            price = random.randrange(5, 12)
            div.items.i = ut.create_menu_button(
                div.items, 
                f'Buy {fruit.title()}',
                div.display,
                buy_fruit
            )
            div.items.i.food = vegetable
            div.items.i.type = 'vegetable'
            div.items.i.stamina_restore = self.fruit_list[fruit]
            div.items.i.price = price
            div.items.i.on('mouseenter', show_fruit_info)

    ut.update_time(60, header, player)
    market_div = ut.new_div(self.display)
    market_div.items = ut.new_div(market_div)
    market_div.display = ut.new_div(market_div)
    for i in range(10):
        fruit = random.choice(lists.fruit)
        price = random.randrange(5, 12)
        market_div.items.i = ut.create_menu_button(
            market_div.items, 
            f'Buy {fruit.title()}',
            market_div.display,
            buy_fruit
        )
        market_div.items.i.stamina_restore = self.fruit_list[fruit]
        market_div.items.i.price = price
        market_div.items.i.on('mouseenter', show_fruit_info)


def buy_menu(self, msg):

    def buy_menu_button_maker(div, text, function, stat, cost, qty):
        button = ut.create_button(div, text, function)
        button.stat = stat
        button.cost = cost
        button.qty = qty
        button.desk = self.desk
        return button

    def shop_button(div, text, function):
        b = ut.create_button(div, text, function)
        b.desk = self.desk
        b.display = self.display
        b.fruit_list = self.fruit
        b.vegetable_list = self.vegetable
        return b
    
    global header
    global player
    
    player = self.player
    header = self.header

    self.display.delete()
    self.display.market = shop_button(
        self.display,
        'Market',
        visit_market
    )
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
        100
    )
    self.display.buy_ink = buy_menu_button_maker(
        self.display,
        "Buy Ink @ $5/50ml",
        buy_desk_item,
        "Ink",
        5,
        50
    )
    pass
