# import libtcod as tcod
import re
import random
import datetime
import book
import math
import player as pr
import justpy as jp
import argparse

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

    new_div = jp.Div(a=webpage, classes="grid grid-cols-3 ")
    new_div.paper = desk_item(new_div, "Paper Tray", player['Desk']['Paper'])
    new_div.ink = desk_item(new_div, "Inkwell", player['Desk']['Ink'])
    new_div.pen = desk_item(new_div, "Pen Holder", player['Desk']['Pen'])
    return new_div


def header_maker(webpage, header_class, player):
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


def library_display_maker(webpage, lib_class, player, player_header, desk):
    library_display = jp.Div(
        a=webpage,
        classes=lib_class + "grid-cols-3 divide-solid divide-black m-2 "
    )
    library_display.text_div = jp.Div(
        a=library_display,
        classes="row-span-full col-span-1 "
    )
    library_display.transcribe_area = jp.Div(
        a=library_display,
        classes='mx-4 col-span-2 col-start-2 p-4'
    )
    library_display.text_div.desc_box = jp.Div(
        a=library_display.text_div,
        text="Choose a book from the list",
        classes="justify-self-center "
    )
    library_display.book_select = jp.Select(
        a=library_display,
        change=describe_book,
        classes=header_base_dark + 'mx-6 h-8 col-start-1 '
    )

    for i in range(len(player['Library'])):
        library_display.book_select.add(
            jp.Option(
                text=player['Library'][i]['Title'],
                value=i,
                text_div=library_display.text_div
            )
        )
    ld = library_display.book_select
    ld.text_div = library_display.text_div
    ld.player = player
    ld.header = player_header
    ld.desk = desk
    ld.transcribe_area = library_display.transcribe_area
    return library_display


def describe_book(self, msg):
    book = self.player['Library'][int(self.value)]

    if book['Transcript Started'] is True:
        button_text = f"Continue \"{book['Title']}\" Transcript"
    else:
        button_text = f"Transcribe \"{book['Title']}\""

    self.text_div.delete()
    self.text_div.desc_box = jp.Div(
        a=self.text_div,
        classes=base_class_dark + 'col-span-1 row-start-2 '
    )
    self.text_div.desc_box.description = jp.Div(
        a=self.text_div.desc_box,
        classes=base_class_dark + 'rounded-full bg-indigo-300 p-5 '
    )
    self.text_div.desc_box.description.text = (
        f"This {book['Type']} is titled \"{book['Title']}\". "
        f"Written by {book['Author']}, "
        f"it is a popular work in the {book['Genre']} genre. "
        f"It consists of {book['Word Count']} words. "
        f"Buyers might pay {book['Transcript Reward']} money."
    )

    self.text_div.desc_box.choose_book = create_menu_button(
        self.text_div.desc_box,
        button_text,
        self.text_div.desc_box,
        start_transcription)
    cb = self.text_div.desc_box.choose_book
    cb.book = book
    cb.player = self.player
    cb.header = self.header
    cb.desk = self.desk
    cb.transcribe_area = self.transcribe_area
    pass

def start_transcription(self, msg):

    def set_transcript_attributes():
            if self.book['Transcript Started'] is False:
                self.book['Transcript Started'] = True
                self.book.update({
                    'Has Supplies': False,
                    'Words Transcribed': 0,
                    'Transcription Complete': False,
                    'Errors': 0,
                    'Is Proofread': False
                })
            pass

    def transcript_div(main_div, text):
        div = jp.Div(a=main_div)
        div.text = text
        return div

    def time_estimate():
        if self.book["Familiarity"] == 0:
            self.book["Familiarity"] += 0.1
        words_left = self.book['Word Count'] - self.book['Words Transcribed']
        base_write = self.player['Skills']['Base Write']
        write_skill = self.player['Skills']['Write']
        base_estimate = words_left / (base_write * write_skill)
        core_time = (base_estimate * 0.75)
        learning_curve = (base_estimate * (0.10 / self.book["Familiarity"]))
        final_estimate = core_time + learning_curve + 1
        self.time_estimate = math.floor(final_estimate)
        return self.time_estimate

    def supply_list():
        wps = self.player['Desk']['Pen']['Words Per Sheet']
        wpm = self.player['Desk']['Ink']['Words Per ml']
        sheets_needed = math.ceil(self.book['Word Count'] / wps)
        self.sheets = sheets_needed
        ink_needed = math.ceil(self.book['Word Count'] / wpm)
        self.ink = ink_needed
        return f"{sheets_needed} sheets of paper, {ink_needed} ml of ink"

    def can_allocate():
        enough_ink = False
        enough_paper = False
        if self.player['Desk']['Ink']['Milliliters'] >= self.ink:
            enough_ink = True
        if self.player['Desk']['Paper']['Sheets'] >= self.sheets:
            enough_paper = True

        if enough_paper and enough_ink:
            self.enough_supplies = True
            return "You can allocate supplies for this transcription."
        else:
            return "You are missing some supplies."

    def allocate_supplies(self, msg):
        if self.book['Has Supplies'] is False:
            self.player['Desk']['Paper']['Sheets'] -= self.sheets
            self.player['Desk']['Ink']['Milliliters'] -= self.ink
            self.book['Has Supplies'] = True
            for i in self.desk.ink.components:
                if 'Milliliters' in i.text:
                    i.text = f"Milliliters: {self.player['Desk']['Ink']['Milliliters']}"
            for i in self.desk.paper.components:
                if 'Sheets' in i.text:
                    i.text = f"Sheets: {self.player['Desk']['Paper']['Sheets']}"
        transcription_info()
        pass

    def validate_input(self, msg):
        if self.value > self.max:
            self.value = self.max
        self.transcribe.label.text = f'Write for {self.value} minutes'
        self.transcribe.time = self.value
        pass

    def write_transcript(self, msg):
        def fatigue_calculator():
            current_tiredness = max(1, self.player['Fatigue'])
            return random.randrange(0, current_tiredness)

        def words_written(fatigue):
            total_words = self.book["Word Count"]
            true_time_written = self.time / max(current_fatigue, 1)
            percent_complete = round(true_time_written / self.estimate, 2)
            return math.floor(total_words * percent_complete)

        def error_calc(comp_words, fatigue):
            pen_errors = self.player['Desk']['Pen']['Error Rate']
            potential_errors = random.randrange(0, comp_words)
            potential_pen_errors = pen_errors * fatigue
            return int(potential_pen_errors * potential_errors)

        def refresh_stamina():
            stamina_used = self.time * self.player['Stamina Per Minute']
            if self.player['Stamina'] - stamina_used < 0:
                self.player['Fatigue'] += max(1, self.player['Fatigue'])
            self.player['Stamina'] -= stamina_used
            stamina_banner = self.header.stamina_banner
            stamina_banner.label.text = f'Stamina: {self.player["Stamina"]}'
            pass

        def increment_time():
            self.player['Time'] += datetime.timedelta(minutes=self.time)
            time_banner = self.header.time_banner
            time_banner.label.text = f'Time: {self.player["Time"]}'
            pass

        def stamina_check():
            if self.player['Stamina'] > 0:
                return True
            else:
                return False

        transcript_complete = self.book['Transcription Complete']
        enough_stamina = stamina_check()
        if not transcript_complete and enough_stamina:

            total_words = self.book["Word Count"]

            current_fatigue = fatigue_calculator()

            completed_words = words_written(current_fatigue)

            self.book['Words Transcribed'] += completed_words
            if self.book['Words Transcribed'] >= total_words:
                self.book['Words Transcribed'] = total_words
                if self.book['Familiarity'] < 1:
                    self.book['Familiarity'] += 0.1
                self.book['Transcription Complete'] = True

            self.book['Errors'] += error_calc(completed_words, current_fatigue)
            refresh_stamina()
            increment_time()
            transcription_info()
        pass

    def proofread_transcript(self, msg):
        def refresh_stamina():
            stamina_used = self.time * self.player['Stamina Per Minute']
            if self.player['Stamina'] - stamina_used < 0:
                self.player['Fatigue'] += max(1, self.player['Fatigue'])
            self.player['Stamina'] -= stamina_used
            stamina_banner = self.header.stamina_banner
            stamina_banner.label.text = f'Stamina: {self.player["Stamina"]}'
            pass

        def increment_time():
            self.player['Time'] += datetime.timedelta(minutes=self.time)
            time_banner = self.header.time_banner
            time_banner.label.text = f'Time: {self.player["Time"]}'
            pass

        skill_set = self.player['Skills']
        read_speed = skill_set['Base Read'] * skill_set['Read']
        self.time = math.ceil(self.book['Word Count'] / read_speed)
        self.book['Is Proofread'] = True
        refresh_stamina()
        increment_time()
        transcription_info()
        pass

    def correct_transcript(self, msg):
        pass

    def find_buyer(self, msg):
        def increment_time(time):
            self.player['Time'] += datetime.timedelta(minutes=time)
            time_banner = self.header.time_banner
            time_banner.label.text = f'Time: {self.player["Time"]}'
            pass

        def decrement_stamina(loss):
            self.player['Stamina'] -= max(loss * self.player['Fatigue'], 1)
            stamina_banner = self.header.stamina_banner
            stamina_banner.label.text = f'Stamina: {self.player["Stamina"]}'
            pass

        popularity_discount = 120 - self.book['Popularity']
        price_modifier = random.randrange(1, popularity_discount)
        price_in_cents = self.book['Transcript Reward'] * price_modifier
        transcript_price = math.ceil(price_in_cents / 100)
        increment_time(60)
        decrement_stamina(1)
        self.price.price = transcript_price
        self.price.label.text = f'Sell for {transcript_price}'

        pass

    def sell_work(self, msg):
        self.player['Money'] += self.price
        m = self.header.money_banner
        m.label.text = f'Money: {self.player["Money"]}'
        attributes_to_remove = [
            'Has Supplies',
            'Words Transcribed',
            'Transcription Complete',
            'Errors',
            'Is Proofread'
        ]
        for i in attributes_to_remove:
            self.book.pop(i)
        self.book['Transcript Started'] = False
        self.book['Transcripts Sold'] += 1
        self.book['Popularity'] += 10
        transcription_info()
        pass

    def transcription_info():
        def basic_info():
            self.transcribe_area.title_line = transcript_div(
                self.transcribe_area,
                f'Title: {self.book["Title"]}'
            )

            self.transcribe_area.word_count = transcript_div(
                self.transcribe_area,
                f'Number of Words: {self.book["Word Count"]}'
            )

            self.transcribe_area.words_transcribed = transcript_div(
                self.transcribe_area,
                f'Words Transcribed: {self.book["Words Transcribed"]}'
            )
            pass

        def allocate_supply_info():
            self.transcribe_area.supplies_needed = transcript_div(
                self.transcribe_area,
                (
                    'Supplies needed: '
                    f'{supply_list()}'
                )
            )

            self.transcribe_area.can_allocate = transcript_div(
                self.transcribe_area,
                f'{can_allocate()}'
            )

            if self.enough_supplies is True:
                self.transcribe_area.allocate_supplies = create_button(
                    self.transcribe_area,
                    "Allocate Supplies",
                    allocate_supplies
                )
                a = self.transcribe_area.allocate_supplies
                a.sheets = self.sheets
                a.ink = self.ink
                a.desk = self.desk
                a.player = self.player
                a.header = self.header
                a.book = self.book
            pass

        def transcript_progress():
            self.transcribe_area.words_transcribed = transcript_div(
                self.transcribe_area,
                (
                    'Estimated Time to Complete: '
                    f'{time_estimate()} minutes'
                )
            )
            self.transcribe_area.time_picker = transcript_div(
                self.transcribe_area,
                'Write for how many minutes?  '
            )
            self.transcribe_area.time_picker.input = jp.InputChangeOnly(
                type='number',
                min=0,
                max=self.time_estimate,
                a=self.transcribe_area.time_picker,
                change=validate_input,
                classes="w-12 rounded text-indigo "
            )

            self.transcribe_area.time_picker.transcribe = create_button(
                self.transcribe_area,
                f'Write for {self.time_estimate} minutes',
                write_transcript
            )
            t = self.transcribe_area.time_picker.transcribe
            t.time = self.time_estimate
            t.desk = self.desk
            t.book = self.book
            t.player = self.player
            t.header = self.header
            t.estimate = self.time_estimate
            self.transcribe_area.time_picker.input.transcribe = t
            pass

        def proofread_info():
            def correct_and_sell():
                self.transcribe_area.error_count = transcript_div(
                    self.transcribe_area,
                    (
                        f"Errors Found: "
                        f"{self.book['Errors']}"
                    )
                )
                if self.book['Errors'] > 0:
                    self.transcribe_area.correct = create_button(
                        self.transcribe_area,
                        'Correct Transcript',
                        correct_transcript
                    )
                else:
                    self.transcribe_area.sell = create_button(
                        self.transcribe_area,
                        'Find Buyer (1 hour)',
                        find_buyer
                    )
                    self.transcribe_area.price = create_button(
                        self.transcribe_area,
                        'Sell Price',
                        sell_work
                    )
                    s = self.transcribe_area.sell
                    s.book = self.book
                    s.player = self.player
                    s.header = self.header
                    s.transcribe_area = self.transcribe_area
                    s.price = self.transcribe_area.price

                    p = self.transcribe_area.price
                    p.header = self.header
                    p.player = self.player
                    p.book = self.book

                pass
            self.transcribe_area.completed_transcript = transcript_div(
                self.transcribe_area,
                "Transcription Complete"
            )
            if self.book['Is Proofread']:
                correct_and_sell()
            else:
                self.transcribe_area.proofread = create_button(
                    self.transcribe_area,
                    'Proofread Transcript',
                    proofread_transcript
                )
                self.transcribe_area.proofread.book = self.book
                self.transcribe_area.proofread.player = self.player
                self.transcribe_area.proofread.header = self.header
            pass

        self.transcribe_area.delete()
        basic_info()

        if self.book['Has Supplies'] is False:
            allocate_supply_info()
        else:
            if self.book['Transcription Complete'] is False:
                transcript_progress()
            else:
                proofread_info()

    set_transcript_attributes()
    transcription_info()
    pass


def buy_snack(self, msg):
    if self.player['Money'] >= self.cost:
        self.player[self.stat] += self.qty
        self.player['Money'] -= self.cost
        self.header.snack_banner.label.text = f'{self.stat}: {self.player[self.stat]}'
        self.header.money_banner.label.text = f'{"Money"}: {self.player["Money"]}'
    pass


def buy_desk_item(self, msg):
    def set_qty_label(stat):
        if stat == 'Paper':
            return 'Sheets'
        if stat == 'Ink':
            return 'Milliliters'
        pass
    qty_label = set_qty_label(self.stat)
    if self.player['Money'] >= self.cost:
        self.player['Desk'][self.stat][qty_label] += self.qty
        self.player['Money'] -= self.cost
        self.header.money_banner.label.text = f'{"Money"}: {self.player["Money"]}'
        for i in self.desk.components:
            if qty_label in i.text:
                i.text = f'{qty_label}: {self.player["Desk"][self.stat][qty_label]}'
    pass


def buy_menu(self, msg):

    def buy_menu_button_maker(div, text, function, stat, cost, qty, header, desk=None):
        button = create_button(div, text, function)
        button.stat = stat
        button.header = header
        button.cost = cost
        button.qty = qty
        button.desk = desk
        button.player = self.player
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


def eat_menu(self, msg):
    self.display.delete()
    self.display.snacks = create_button(self.display, "Eat Snack for 25 Stamina", eat_snack)
    self.display.snacks.header = self.header
    self.display.snacks.player = self.player

    pass

def eat_snack(self, msg):
    if self.player['Snacks'] > 0:
        self.player['Snacks'] += -1
        self.player['Stamina'] += 25
        self.header.snack_banner.label.text = f'Snacks: {self.player["Snacks"]}'
        self.header.stamina_banner.label.text = f'Stamina: {self.player["Stamina"]}'
    pass


def transcribe_menu(self, msg):
    self.display.delete()
    self.display.library_display = library_display_maker(
        self.display,
        library_display_class,
        self.player,
        self.header,
        self.desk
    )

    pass


def main_menu_maker(webpage, header, desk_display, player):

    def main_menu_button_maker(div, text, display, function):
        button = create_menu_button(div, text, display, function)
        button.current_menu = main_desk.button_area.current_menu
        button.header = header
        button.desk = desk_display
        button.player = player
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
        buy_menu
    )
    main_desk.button_area.transcribe = main_menu_button_maker(
        main_desk.button_area,
        "Transcribe",
        main_desk.text_area,
        transcribe_menu
    )
    main_desk.button_area.eat = main_menu_button_maker(
        main_desk.button_area,
        "Self Care",
        main_desk.text_area,
        eat_menu
    )
    return main_desk


def gamemenu():
    wp = jp.WebPage(delete_flag=True)
    player = pr.new_player()
    header = header_maker(wp, header_grid, player)
    desk_display = desk_area(wp, player)
    main_desk = main_menu_maker(wp, header, desk_display, player)
    return wp


jp.justpy(gamemenu, host='0.0.0.0', port=8080)
