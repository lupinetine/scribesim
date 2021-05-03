# import libtcod as tcod
import re
import random
import datetime
import book
import player as pr
import justpy as jp
import icecream as ic


# CLASSES CSS #
base_class = "text-white rounded text-center "
base_class_dark = "text-indigo rounded text-left"

library_display_class = "ring-4 bg-gray-300 col-span-auto "
grid_base = "grid auto-cols-auto "
button_base = "m-3 ring-4 ring-black-600 text-gray font-bold rounded "

player_name = base_class + "m-1 font-black bg-indigo-500 "
header_base = base_class + "m-2 font-bold justify-center "
button_menu = button_base + " bg-blue-600 p-2 inline "

header_grid = grid_base + "ring-4 ring-indigo-600 ring-offset-4 "

desk_item_header = header_base + (
    "col-span-1 "
    "ring-4 "
    "bg-indigo-300 "
    "hover:bg-indigo-500 "
)
blue_header = header_base + "bg-blue-500 "
green_header = header_base + "bg-green-500 "
red_header = header_base + "bg-red-500 "
pink_header = header_base + "bg-pink-500 "


def buy_supplies(supply, quantity):
    print(f"Okay, going to the store and buying {supply}", end="")
    print(f" for a total of {player['Desk'][supply] + quantity}.")
    player['Desk'][supply] += quantity
    pass


def describe_book(self, msg):
    book = player['Library'][self.value]
    self.text_div.title_line.text = ""
    self.title_line.text = (
        f"This {book['Type']} is titled \"{book['Title']}\". "
        f"It is written by {book['Author']}."
    )
    self.desc_line.text = (
        f"It is a popular work in the {book['Genre']} genre "
        f"and consists of {book['Word Count']} words."
    )
    self.payout_line.text = (
        f"The base price for completing the transcript "
        f"is {book['Transcript Reward']} money."
    )
    self.choose_book.label.text = f"Choose \"{book['Title']}\""
    pass


def set_stat(stat, amount):
    if player[stat] + amount < 0:
        player[stat] = 0
    else:
        player[stat] += amount
    pass


def set_change(self, msg):
    self.button.amount.text = self.value
    self.button.to_change = self.value
    pass


def set_stat_and_display(self, msg):
    set_stat(self.stat, self.to_change)
    self.banner.label.text = f'{self.stat}: {player[self.stat]}'
    pass


def player_div_banner(stat, div, classes):
    new_div = jp.Div(
        a=div,
        classes=classes
    )
    new_div.label = jp.P(
        text=f'{stat}: {player[stat]}',
        a=new_div,
        classes=classes + "justify-self-center "
    )
    return new_div


def create_menu_button(
    dest_div,
    button_text,
    display_area,
    click_function,
    button_classes=button_menu
):
    button = create_button(
        dest_div,
        button_text,
        click_function,
        button_classes
    )
    button.display = display_area
    return button


def create_button(dest_div, button_text, click_function, button_classes=button_menu):
    button = create_empty_button(dest_div, button_text, button_classes)
    button.on('click', click_function)
    return button


def create_empty_button(dest_div, button_text, button_classes=button_menu):
    button = jp.Button(a=dest_div, classes=button_classes)
    button.label = jp.P(a=button, text=button_text)
    return button


def desk_area(webpage, player):
    new_div = jp.Div(a=webpage, classes="grid grid-cols-3 ")
    new_div.paper = desk_item(new_div, "Paper Tray", player['Desk']['Paper'])
    new_div.ink = desk_item(new_div, "Inkwell", player['Desk']['Ink'])
    new_div.pen = desk_item(new_div, "Pen Holder", player['Desk']['Pen'])
    return new_div


def desk_item(desk_div, header_text, item_entry):
    new_div = jp.Div(a=desk_div, classes=desk_item_header)
    new_div.header = jp.P(a=new_div,
                          classes=player_name,
                          text=header_text)
    for k, v in item_entry.items():
        new_div.k = jp.P(a=new_div,
                         classes=base_class,
                         text=f'{k}: {v}')
    return new_div


def header_maker(webpage, header_class):
    header = jp.Div(a=webpage, classes=header_class)
    header.name_banner = jp.Div(
        text=f'{player["Name"]}, {player["Job"]}',
        a=header,
        classes=player_name + "col-span-4 "
    )
    header.stamina_banner = player_div_banner("Stamina", header, red_header)
    header.money_banner = player_div_banner("Money", header, green_header)
    header.snack_banner = player_div_banner("Snacks", header, pink_header)
    header.time_banner = player_div_banner("Time", header, blue_header)
    return header


def library_display_maker(webpage, lib_class):
    library_display = jp.Div(
        a=webpage,
        classes=lib_class + "overflow-x-auto grid-row-1 "
    )
    library_display.text_div = jp.Div(
        a=webpage,
        classes=lib_class + "border-5 border-black "
    )
    library_display.text_div.title_line = jp.Div(
        a=library_display.text_div,
        classes=base_class_dark
    )
    library_display.text_div.desc_line = jp.Div(
        a=library_display.text_div,
        classes=base_class_dark
    )
    library_display.text_div.payout_line = jp.Div(
        a=library_display.text_div,
        classes=base_class_dark
    )
    library_display.text_div.choose_book = create_button(
        library_display.text_div,
        "Choose a Book to Start",
        start_transcription
    )

    for i in range(len(player['Library'])):
        library_display.i = create_button(library_display,
                                          player['Library'][i]['Title'],
                                          describe_book)
        library_display.i.value = i
        library_display.i.text_div = library_display.text_div
        library_display.i.title_line = library_display.text_div.title_line
        library_display.i.desc_line = library_display.text_div.desc_line
        library_display.i.payout_line = library_display.text_div.payout_line
        library_display.i.choose_book = library_display.text_div.choose_book
    return library_display


def transcribe_menu(self, msg):
    self.display.delete()
    pass


def start_transcription():
    pass


def can_afford(amount):
    if player['Money'] >= amount:
        return True
    else:
        return False


def buy_snack(self, msg):
    if can_afford(self.cost):
        player[self.stat] += self.qty
        player['Money'] -= self.cost
        self.header.snack_banner.label.text = f'{self.stat}: {player[self.stat]}'
        self.header.money_banner.label.text = f'{"Money"}: {player["Money"]}'
    pass


def set_qty_label(stat):
    if stat == 'Paper':
        return 'Sheets'
    if stat == 'Ink':
        return 'Milliliters'
    pass


def buy_desk_item(self, msg):
    qty_label = set_qty_label(self.stat)
    if can_afford(self.cost):
        player['Desk'][self.stat][qty_label] += self.qty
        player['Money'] -= self.cost
        self.header.money_banner.label.text = f'{"Money"}: {player["Money"]}'
        for i in self.desk.components:
            if qty_label in i.text:
                i.text = f'{qty_label}: {player["Desk"][self.stat][qty_label]}'
    pass


def eat_snack(self, msg):
    if player['Snacks'] > 0:
        player['Snacks'] += -1
        player['Stamina'] += 25
        self.header.snack_banner.label.text = f'Snacks: {player["Snacks"]}'
        self.header.stamina_banner.label.text = f'Stamina: {player["Stamina"]}'
    pass


def buy_menu_button_maker(div, text, function, stat, cost, qty, header, desk=None):
    button = create_button(div, text, function)
    button.stat = stat
    button.header = header
    button.cost = cost
    button.qty = qty
    button.desk = desk
    return button


def buy_menu(self, msg):
    self.display.delete()
    self.display.buy_snacks = buy_menu_button_maker(
        self.display,
        "Buy Snacks @ $5/each",
        buy_snack,
        "Snacks",
        5,
        1,
        self.header
    )
    self.display.buy_paper = buy_menu_button_maker(
        self.display,
        "Buy Paper @ $10/100 sheets",
        buy_desk_item,
        "Paper",
        10,
        100,
        self.header,
        self.desk.paper
    )
    self.display.buy_ink = buy_menu_button_maker(
        self.display,
        "Buy Ink @ $5/50ml",
        buy_desk_item,
        "Ink",
        5,
        50,
        self.header,
        self.desk.ink
    )
    pass


def gamemenu():
    wp = jp.WebPage(delete_flag=True)
    header = header_maker(wp, header_grid)
    desk_display = desk_area(wp, player)
    library_display = library_display_maker(wp, library_display_class)
    main_desk = jp.Div(a=wp, classes=grid_base)
    main_desk.button_area = jp.Div(a=main_desk, classes="ring-4 bg-pink-300 col-span-full ")
    main_desk.text_area = jp.Div(a=main_desk, classes="col-span-full ")
    main_desk.button_area.buy = create_menu_button(main_desk.button_area, "Buy Supplies", main_desk.text_area, buy_menu)    
    main_desk.button_area.buy.header = header
    main_desk.button_area.buy.desk = desk_display
    main_desk.button_area.transcribe = create_menu_button(main_desk.button_area, "Transcribe New Book", main_desk.text_area, transcribe_menu)    
    main_desk.button_area.eat = create_menu_button(main_desk.button_area, "Eat Snack", main_desk.text_area, eat_snack)
    main_desk.button_area.eat.header = header
    return wp


player = pr.new_player()
jp.justpy(gamemenu)
