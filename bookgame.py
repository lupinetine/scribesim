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


def library_display_maker(webpage, lib_class, player, player_header, desk):
    library_display = ut.new_div(
        webpage,
        lib_class + "grid-cols-3 divide-solid divide-black m-2 "
    )
    library_display.text_div = ut.new_div(
        library_display,
        "row-span-full col-span-1 "
    )
    library_display.transcribe_area = ut.new_div(
        library_display,
        'mx-4 col-span-2 col-start-2 p-4'
    )
    library_display.text_div.desc_box = ut.new_div(
        library_display.text_div,
        "object-center "
    )
    library_display.book_select = ut.lib_select(
        library_display.text_div,
        tr.describe_book,
        ut.header_base_dark + 'mx-6 h-8 col-start-1 '
    )

    for i in range(len(player['Library'])):
        library_display.book_select.add(
            ut.lib_option(
                player['Library'][i]['Title'],
                i,
                library_display.text_div
            )
        )
    ld = library_display.book_select
    ld.text_div = library_display.text_div
    ld.player = player
    ld.header = player_header
    ld.desk = desk
    ld.transcribe_area = library_display.transcribe_area
    return library_display


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


def transcribe_menu(self, msg):
    self.display.delete()
    self.display.library_display = library_display_maker(
        self.display,
        ut.library_display_class,
        player,
        header,
        self.desk
    )

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
        transcribe_menu
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
