import utilities as ut 
import random
import lists
import icecream as ic

def create_fruit_list():
    return create_food_list(lists.fruit)


def create_vegetable_list():
    return create_food_list(lists.vegetable)


def create_pastry_list():
    return create_food_list(lists.pastry_base)


def create_food_list(input_list):
    d = {}
    for i in input_list:
        d.update({i: random.randrange(5, 15)})
    return d



def buy_food(self, msg):
    if self.player['Money'] >= self.dict['Price']:
        self.player['Stocks']['Food'].append(self.dict)
        self.stocks['Stocks'].remove(self.dict)
        ut.update_money_banner(self.dict['Price'], self.header, self.player)
        ut.update_food_banner(self.header, self.player)
    print(self.stocks)

    display_market(self.div, self)
    pass


def display_market(div, self):
    print(self.stocks)
    div.delete()
    print(div)
    for i in self.stocks['Stocks']:
        div.i = ut.create_buy_button(
            div,
            f'Buy {i["Name"]}',
            buy_food,
            i,
            self.stocks,
            (
                f'Restores {i["Restore"]} '
                f'for ${i["Price"]}'
            )
        )
        div.i.player = self.player
        div.i.header = self.header




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
    
 
    self.div = ut.store_div(self)
    ic.ic(self.div)
    ut.stock_shelves(self, restock_produce)
    ut.store_display(self, display_market)

