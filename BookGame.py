# import libtcod as tcod
import re
import random
import datetime
import book
import player as pr
import justpy as jp
import icecream as ic

# GLOBALS #


# CLASSES CSS #
base_class = "text-white rounded text-center "
base_class_dark = "text-indigo rounded text-center "

library_display_class = "grid grid-cols-3 divide-x bg-gray-300 col-span-auto "
grid_base = "grid auto-cols-auto "
button_base = "m-3 ring-4 ring-black-600 text-gray font-bold rounded "

player_name = base_class + "m-1 font-black bg-indigo-500 "
header_base = base_class + "m-2 font-bold justify-center "
header_base_dark = base_class_dark + "m-2 font-bold justify-center "
button_menu = button_base + "bg-blue-600 p-2 inline "

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


def describe_book(self, msg):
    book = player['Library'][int(self.value)]
    self.text_div.delete()
    self.text_div.desc_box = jp.Div(
        a=self.text_div,
        classes=base_class_dark + 'col-span-1 '
    )
    self.text_div.desc_box.description = jp.Div(
        a=self.text_div.desc_box,
        classes=base_class_dark + 'rounded-full bg-indigo-300 p-4'
    )
    self.text_div.desc_box.description.text = (
        f"This {book['Type']} is titled \"{book['Title']}\". "
        f"Written by {book['Author']}, "
        f"it is a popular work in the {book['Genre']} genre. "
        f"It consists of {book['Word Count']} words. "
        f"Buyers might pay {book['Transcript Reward']} money."
    )
    if book['Transcript Started'] is True:
        self.text_div.desc_box.choose_book = create_menu_button(
            self.text_div.desc_box,
            f"Continue \"{book['Title']}\" Transcript",
            self.text_div.desc_box,
            continue_transcription)
        self.text_div.desc_box.choose_book.book = book
        self.text_div.desc_box.choose_book.transcribe_area = self.transcribe_area
    else:
        self.text_div.desc_box.choose_book = create_menu_button(
            self.text_div.desc_box,
            f"Transcribe \"{book['Title']}\"",
            self.text_div.desc_box,
            start_transcription)
        self.text_div.desc_box.choose_book.book = book
        self.text_div.desc_box.choose_book.transcribe_area = self.transcribe_area
    pass


def create_menu_button(
    dest_div,
    button_text,
    display_area,
    click_function,
    button_classes=button_menu,
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
        classes=lib_class + "overflow-x-auto grid-row-auto "
    )
    library_display.text_div = jp.Div(
        a=webpage,
        classes=lib_class + " "
    )
    library_display.book_select = jp.Select(a=library_display, change=describe_book, classes=header_base_dark + ' mx-6 ')
    for i in range(len(player['Library'])):
        library_display.book_select.add(
            jp.Option(
                text=player['Library'][i]['Title'],
                value=i,
                text_div=library_display.text_div
            )
        )
    library_display.book_select.text_div = library_display.text_div
    library_display.book_select.transcribe_area = jp.Div(a=library_display, classes='col-span-2 ')
    library_display.book_select.transcribe_area.text = 'Choose a book to start'
    return library_display


def start_transcription(self, msg):
    self.transcribe_area.delete()
    print(self.book)
    self.book['Transcript Started'] = True
    self.book.update({
        'Words Transcribed': 0,
        'Errors': 0,
        'Is Proofread': False
    })
    print(self.book)
    self.text = f'Continue \"{self.book["Title"]}\" Transcript'
    self.transcribe_area.text = f"Title: {self.book['Title']}"
    self.transcribe_area.word_count = jp.Div(a=self.transcribe_area)
    self.transcribe_area.word_count.text = f'Number of Words: {self.book["Word Count"]}'
    self.transcribe_area.words_transcribed = jp.Div(a=self.transcribe_area)
    self.transcribe_area.words_transcribed.text = f'Words Transcribed: {self.book["Words Transcribed"]}'

    # = (self.book['Word Count'])

    pass


def continue_transcription():
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


def buy_desk_item(self, msg):
    def set_qty_label(stat):
        if stat == 'Paper':
            return 'Sheets'
        if stat == 'Ink':
            return 'Milliliters'
        pass
    qty_label = set_qty_label(self.stat)
    if can_afford(self.cost):
        print(qty_label)
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


def buy_menu(self, msg):

    def buy_menu_button_maker(div, text, function, stat, cost, qty, header, desk=None):
        button = create_button(div, text, function)
        button.stat = stat
        button.header = header
        button.cost = cost
        button.qty = qty
        button.desk = desk
        return button

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


def transcribe_menu(self, msg):
    self.display.delete()
    self.display.library_display = library_display_maker(self.display, library_display_class)

    pass


def eat_menu(self, msg):
    self.display.delete()
    self.display.snacks = create_button(self.display, "Eat Snack for 25 Stamina", eat_snack)
    self.display.snacks.header = self.header
    pass


def main_menu_maker(webpage, header, desk_display):

    def main_menu_button_maker(div, text, display, function, header, desk_display):
        button = create_menu_button(div, text, display, function)
        button.current_menu = main_desk.button_area.current_menu
        button.header = header
        button.desk = desk_display
        return button

    main_desk = jp.Div(a=webpage, classes=grid_base)
    main_desk.button_area = jp.Div(
        a=main_desk,
        classes="bg-pink-300 col-span-full focus:ring-4 "
    )
    main_desk.button_area.current_menu = "Home"
    main_desk.text_area = jp.Div(
        a=main_desk,
        classes="col-span-full inline "
    )
    main_desk.button_area.buy = main_menu_button_maker(
        main_desk.button_area,
        "Buy",
        main_desk.text_area,
        buy_menu,
        header,
        desk_display
    )
    main_desk.button_area.transcribe = main_menu_button_maker(
        main_desk.button_area,
        "Transcribe",
        main_desk.text_area,
        transcribe_menu,
        header,
        desk_display
    )
    main_desk.button_area.eat = main_menu_button_maker(
        main_desk.button_area,
        "Self Care",
        main_desk.text_area,
        eat_menu,
        header,
        desk_display
    )
    return main_desk


def gamemenu():
    wp = jp.WebPage(delete_flag=True)
    header = header_maker(wp, header_grid)
    desk_display = desk_area(wp, player)
    main_desk = main_menu_maker(wp, header, desk_display)
    return wp


player = pr.new_player()
jp.justpy(gamemenu)
