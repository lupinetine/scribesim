# import libtcod as tcod
import re
import random
import datetime
import book
import player as pr
import justpy as jp


# CLASSES CSS #
base_class = "text-white rounded text-center "

player_name = base_class + "m-1 font-black bg-indigo-500 "
header_base = base_class + "m-2 font-bold justify-center "

grid_base = "grid auto-cols-auto "
button_base = "m-3 ring-4 ring-black-600 text-gray font-bold rounded "
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
    self.title_line.text = (
        f"This {book['Type']} is titled \"{book['Title']}\". "
        f"It is written by {book['Author']}."
    )
    self.desc_line = (
        f"It is a popular work in the {book['Genre']} genre "
        f"and consists of {book['Word Count']} words."
    )
    self.payout_line = (
        f"The price for completing the transcript "
        f"is {book['Transcript Reward']} money."
    )
    pass


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


def create_menu_button(dest_div, button_text, display_area, click_function):
    button = create_button(dest_div, button_text, click_function)
    button.display = display_area
    return button


def create_button(dest_div, button_text, click_function):
    button = create_empty_button(dest_div, button_text)
    button.on('click', click_function)
    return button


def create_empty_button(dest_div, button_text):
    button = jp.Button(a=dest_div, classes=button_menu)
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


def gamemenu():
    wp = jp.WebPage()
    header = header_maker(wp, header_grid)
    desk_display = desk_area(wp, player)
    library_display = jp.Div(a=wp, classes="ring-4 bg-gray-300 col-span-full ",)
    library_display.text_div = jp.Div(a=wp, classes="ring-4 bg-gray-300 col-span-full ")
    library_display.text_div.title_line = jp.Div(a=library_display.text_div, classes=base_class)
    library_display.text_div.desc_line = jp.Div(a=library_display.text_div, classes=base_class)
    library_display.text_div.payout_line = jp.Div(a=library_display.text_div, classes=base_class)
    library_display.book1 = create_button(library_display,
                                          player['Library'][0]['Title'],
                                          describe_book)
    library_display.book1.value = 0
    library_display.book1.text_div = library_display.text_div
    library_display.book1.title_line = library_display.text_div.title_line
    library_display.book1.desc_line = library_display.text_div.desc_line
    library_display.book1.payout_line = library_display.text_div.payout_line
    button_area = jp.Div(a=wp, classes="ring-4 bg-pink-300 col-span-full ")
    text_area = jp.Div(a=wp, classes="col-span-full ")
    return wp


player = pr.new_player()
jp.justpy(gamemenu)
