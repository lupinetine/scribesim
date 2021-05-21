# import libtcod as tcod
import care
import shop
import player as pr
import utilities as ut 
import transcription as tr

def desk_area(webpage):
    new_div = ut.new_div(webpage, "grid grid-cols-3 ")
    ut.update_desk_banner(new_div, player)
    return new_div


def header_maker(webpage):
    header = ut.new_div(webpage, ut.header_grid)
    header.name_banner = ut.text_div(
        header,
        f'{player["Name"]}, {player["Job"]}',
        ut.player_name + "col-span-4 "
    )
    header.stamina_banner = ut.player_div_banner(
        "Stamina",
        player,
        header,
        ut.stamina_header(player['Fatigue'])
    )
    header.money_banner = ut.player_div_banner(
        "Money",
        player,
        header,
        ut.green_header
    )
    header.food_banner = ut.player_div_banner(
        "Food",
        player['Stocks'],
        header,
        ut.pink_header
    )
    header.time_banner = ut.player_div_banner(
        "Time",
        player,
        header,
        ut.blue_header
    )
    return header


def main_menu_maker(webpage, desk_display):

    def main_menu_button_maker(div, text, function, display):
        button = ut.create_menu_button(div, text, function, display)
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
        shop.buy_menu,
        main_desk.text_area
    )
    main_desk.button_area.buy.market = shop.create_market_dictionary()
 
    main_desk.button_area.transcribe = main_menu_button_maker(
        main_desk.button_area,
        "Transcribe",
        tr.transcribe_menu,
        main_desk.text_area
    )

    main_desk.button_area.self_care = main_menu_button_maker(
        main_desk.button_area,
        "Self Care",
        care.care_menu,
        main_desk.text_area
    )
    return main_desk


def gamemenu():
    global player
    global header

    wp = ut.new_webpage()
    player = pr.new_player()
    header = header_maker(wp)
    desk_display = desk_area(wp)
    main_desk = main_menu_maker(wp, desk_display)
    return wp


ut.run_game(gamemenu)
