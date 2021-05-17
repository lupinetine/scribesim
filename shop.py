import utilities as ut
import random
import lists


def buy_snack(self, msg):
    if player['Money'] >= self.cost:
        ut.update_money_banner(self.cost, header, player)
        player[self.stat] += self.qty
        header.snack_banner.label.text = f'{self.stat}: {player[self.stat]}'
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


def create_fruit_list():
    return create_food_list(lists.fruit)


def create_vegetable_list():
    return create_food_list(lists.vegetable)


def create_pastries_list():
    return create_food_list(lists.pastries)


def create_food_list(input_list):
    dict = {}
    for i in input_list:
        dict.update({i: random.randrange(1, 15)})
    return dict


def buy_market_item(self, msg):
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

    def lookup_food_type(food_type):
        f = []
        if food_type is 'vegetable':
            f.append(lists.vegetable)
            f.append(self.vegetable_list)
        elif food_type is 'fruit':
            f.append(lists.fruit)
            f.append(self.fruit_list)
        else:
            f.append(lists.pastries)
            f.append(self.pastries_list)
        return f

    def stock_food(div, food_type, display):
        f = lookup_food_type(food_type)
        food_list = f[0]
        food_lookup = f[1]
        food = random.choice(food_list)
        price = random.randrange(5, 12)
        print(price)
        div.food = ut.create_menu_button(
            div,
            f'Buy {food.title()}',
            display,
            buy_food
        )
        div.food.food = food
        div.food.food_type = food_type
        div.food.stamina_restore = food_lookup[food]
        div.food.price = price
        div.food.on('mouseenter', show_food_info)

    def restock_produce(div):
        for i in range(10):
            print('miao')
            stock_food(div.items, 'vegetable', div.display)
            stock_food(div.items, 'fruit', div.display)
        div.restocked = True

    ut.update_time(60, header, player)
    market_div = ut.new_div(self.display)
    market_div.items = ut.new_div(market_div)
    market_div.display = ut.new_div(market_div)
    restock_produce(market_div)
    # if player['Time'].hour() < 6 and market_div.restocked is False:
    #     restock_produce(market_div)
    # elif player['Time'].hour() > 16:
    #     market_div.restocked = False


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
        b.pastries_list = self.pastries
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
