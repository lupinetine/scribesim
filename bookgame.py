# import libtcod as tcod
import random
import datetime
import math
import care
import shop
import player as pr
import utilities as ut 
import transcription as tr

def desk_area(webpage, player):
    new_div = ut.new_div(webpage, "grid grid-cols-3 ")
    new_div.paper = ut.desk_item(new_div, "Paper Tray", player['Desk']['Paper'])
    new_div.ink = ut.desk_item(new_div, "Inkwell", player['Desk']['Ink'])
    new_div.pen = ut.desk_item(new_div, "Pen Holder", player['Desk']['Pen'])
    return new_div


def header_maker(webpage):
    header = ut.new_div(webpage, ut.header_grid)
    header.name_banner = ut.new_div(
        header,
        ut.player_name + "col-span-4 "
    )
    header.name_banner.text = f'{player["Name"]}, {player["Job"]}'
    header.stamina_banner = ut.player_div_banner(
        "Stamina",
        header,
        ut.stamina_header(player['Fatigue']),
        player)
    header.money_banner = ut.player_div_banner(
        "Money",
        header,
        ut.green_header,
        player)
    header.snack_banner = ut.player_div_banner(
        "Snacks",
        header,
        ut.pink_header,
        player)
    header.time_banner = ut.player_div_banner(
        "Time",
        header,
        ut.blue_header,
        player)
    return header


def care_menu(self, msg):
    def care_button(div, text, click):
        b = ut.create_button(div, text, click)
        b.header = header
        b.player = player
        return b
    self.display.delete()
    self.display.snacks = care_button(
        self.display, 
        "Eat Snack for 25 Stamina", 
        eat_snack
    )
    pass

def eat_snack(self, msg):
    if player['Snacks'] > 0:
        player['Snacks'] += -1
        player['Stamina'] += 25
        header.snack_banner.label.text = f'Snacks: {player["Snacks"]}'
        header.stamina_banner.label.text = f'Stamina: {player["Stamina"]}'
    pass





def main_menu_maker(webpage, desk_display):

    def main_menu_button_maker(div, text, display, function):
        button = ut.create_menu_button(div, text, display, function)
        button.current_menu = main_desk.button_area.current_menu
        button.header = header
        button.desk = desk_display
        button.player = player
        return button

    main_desk = ut.new_div(webpage, ut.grid_base)
    main_desk.button_area = ut.new_div(
        main_desk,
        "bg-pink-300 col-span-full focus:ring-4 "
    )
    main_desk.button_area.current_menu = "Home"
    main_desk.text_area = ut.new_div(
        main_desk,
        "col-span-full inline "
    )
    main_desk.button_area.buy = main_menu_button_maker(
        main_desk.button_area,
        "Buy",
        main_desk.text_area,
        shop.buy_menu
    )
    main_desk.button_area.transcribe = main_menu_button_maker(
        main_desk.button_area,
        "Transcribe",
        main_desk.text_area,
        tr.transcribe_menu
    )
    main_desk.button_area.self_care = main_menu_button_maker(
        main_desk.button_area,
        "Self Care",
        main_desk.text_area,
        care.care_menu
    )
    return main_desk


def gamemenu():
    global player
    global header

    wp = ut.new_webpage()
    player = pr.new_player()
    header = header_maker(wp)
    desk_display = desk_area(wp, player)
    main_desk = main_menu_maker(wp, desk_display)
    return wp


ut.run_game(gamemenu)
