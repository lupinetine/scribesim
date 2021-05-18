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
        dict.update({i: random.randrange(5, 15)})
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
            f'This {self.dict["Type"]} restores '
            f'{self.dict["Restore"]} '
            f'stamina and costs {self.dict["Price"]}'
        ),
        ut.base_class_dark + 'justify-center w-1/4 max-w-min bg-gray-700 '
    )
    pass


def visit_market(self, msg):

    def display_stocks(div):
        print('trying to display stocks')
        for i in self.current_stock:
            div.i = ut.create_menu_button(
                div,
                f'Buy {i["Name"]}',
                div.display,
                buy_food
            )
            print('button made')
            div.i.dict = i
            div.i.on('mouseenter', show_food_info)

    def stock_food(food_list):
        food = random.choice(food_list)
        if food_list is lists.vegetable:
            food_type = 'vegetable'
            restore = self.vegetable_list[food]
        elif food_list is lists.fruit:
            food_type = 'fruit'
            restore = self.fruit_list[food]
        else:
            food_type = 'pastry'
            restore = self.pastries_list[food]
        price = random.randrange(5, 12)

        return {
            'Name': food, 
            'Type': food_type, 
            'Restore': restore,
            'Price': price
        }

    def choose_produce():
        print('choosing a produce type')
        if bool(random.getrandbits(1)):
            print('it\'s veg!')
            return lists.vegetable
        else:
            return lists.fruit

    def restock_produce():
        self.current_stock = []
        for _ in range(random.randrange(4, 20)):
            print('adding a new food')
            self.current_stock.append(stock_food(choose_produce()))

    ut.update_time(60, header, player)
    self.display.options.delete()
    print('picklecat')
    market_div = ut.new_div(self.display.options)
    market_div.display = ut.new_div(market_div)
    if player['Time'].hour < 9 and self.restocked is False:
        print('restocking time')
        restock_produce()
        self.restocked = True
    elif player['Time'].hour > 16 and self.restocked is True:
        self.restocked = False
    display_stocks(market_div)


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
        b.restocked = False
        b.current_stock = []
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

    self.display.options = ut.new_div(self.display)
    self.display.market.options = self.display.options
    
    pass
