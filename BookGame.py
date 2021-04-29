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

header_class = grid_base + "ring-4 ring-indigo-600 ring-offset-4 "
blue_header = header_base + "bg-blue-500 "
green_header = header_base + "bg-green-500 "
red_header = header_base + "bg-red-500 "
pink_header = header_base + "bg-pink-500 "


def buy_supplies(supply, quantity):
    print(f"Okay, going to the store and buying {supply}", end="")
    print(f" for a total of {player['Desk'][supply] + quantity}.")
    player['Desk'][supply] += quantity
    pass


def describe_book(book):
    print("*********")
    print(f"This {book['Type']} is titled \"{book['Title']}\". It is written by {book['Author']}.")
    print(f"It is a popular work in the {book['Genre']} genre and consists of {book['Word Count']} words.")
    print(f"The price for completing the transcript is {book['Transcript Reward']} dollaridoos.")
    print("*********\n")
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
    button = jp.Button(a=dest_div, classes=button_menu)
    button.label = jp.P(a=button, text=button_text)
    button.display = display_area
    button.on('click', click_function)
    return button


def view_desk():
     
    pass


def view_library():
    pass


def view_shop():
    pass


# def mod_div(stat, banner, webpage):
#     new_div = jp.Div(
#         a=webpage,
#         classes=grid_base
#     )

#     change = jp.InputChangeOnly(
#         type='number',
#         a=new_div,
#         classes="w-1/4 rounded col-span-1 "
#     )
#     button = jp.Button(
#         a=new_div,
#         classes=button_base + "w-1/4 bg-red-600 "
#     )
#     button.to_change = 0
#     button.stat = stat
#     button.label = jp.P(
#         text=f'Change player {button.stat} by ',
#         a=button,
#         classes="inline "
#     )
#     button.amount = jp.P(
#         text=button.to_change,
#         a=button,
#         classes="inline "
#     )
#     button.banner = banner
#     button.on('click', set_stat_and_display)
#     change.button = button
#     change.on('change', set_change)
#     return new_div


def gamemenu():
    wp = jp.WebPage()
    header = jp.Div(a=wp, classes=header_class)
    name_banner = jp.Div(
        text=f'{player["Name"]}, {player["Job"]}',
        a=header,
        classes=player_name + "col-span-4 "
    )
    stamina_banner = player_div_banner("Stamina", header, red_header)
    money_banner = player_div_banner("Money", header, green_header)
    snack_banner = player_div_banner("Snacks", header, pink_header)
    time_banner = player_div_banner("Time", header, blue_header)
    button_area = jp.Div(a=wp, classes="ring-4 bg-pink-300 col-span-full ")
    text_area = jp.Div(a=wp, classes="col-span-full")
    text_area.button_div = jp.Div(a=text_area,
                                  classes="bg-gray-400 overflow-x-auto ")
    text_area.text_div = jp.Div(a=text_area,
                                classes="bg-gray-400 overflow-x-auto ")
    desk_button = create_menu_button(button_area,
                                     'View Inventory',
                                     text_area,
                                     view_desk)
    library_button = create_menu_button(button_area,
                                        'View Library',
                                        text_area,
                                        view_library)
    shop_button = create_menu_button(button_area,
                                        'Visit Shop',
                                        text_area,
                                        view_shop)
    # money_div = mod_div("Money", money_banner, wp)

    return wp


player = pr.new_player()
jp.justpy(gamemenu)
 