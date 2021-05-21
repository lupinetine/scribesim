import utilities as ut


def care_menu(self, msg):

    global header
    global player

    player = self.player
    header = self.header

    def care_button(div, text, click, display):
        b = ut.create_menu_button(div, text, click, display)
        return b

    self.display.delete()
    self.display.buttons = ut.new_div(self.display)
    self.display.options = ut.new_div(self.display)
    self.display.food = care_button(
        self.display.buttons,
        "Eat Food",
        show_food,
        self.display.options
    )
    self.display.snacks = care_button(
        self.display.buttons,
        "Sleep for 8 hours",
        sleep,
        self.display.options
    )
    pass


def show_food(self, msg):
    display_food(self.display)


def display_food(div):
    div.delete()
    for i in player['Stocks']['Food']:
        div.i = ut.create_button(
            div,
            f'Eat {i["Name"]}',
            eat_food,
            ut.food_menu
        )
        div.i.info = ut.new_para(div.i, 'text-xs ')
        div.i.info.text = (f'Restores {i["Restore"]} Stamina')
        div.i.dict = i
        div.i.div = div

def eat_food(self, msg):    
    ut.update_stamina_banner(-self.dict['Restore'], header, player)
    player['Stocks']['Food'].remove(self.dict)
    ut.update_food_banner(header, player)
    display_food(self.div)
    

def sleep(self, msg):
    player['Fatigue'] -= 8
    if player['Fatigue'] < -2:
        player['Fatigue'] = -2
    ut.update_time(480, header, player)
    ut.update_stamina_banner(-100, header, player)
    pass
