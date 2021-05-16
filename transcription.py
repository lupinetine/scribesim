import math
import random
import datetime
import utilities as ut

def set_book_text(book):
    global current_price
    current_price = calc_price(book)
    return (
        f"This {book['Type']} is titled \"{book['Title']}\". "
        f"Written by {book['Author']}, "
        f"it is a {describe_popularity(book)} work in "
        f"the {book['Genre']} genre. "
        f"It consists of {book['Word Count']} words. "
        f"You've seen it sell for ${current_price}."
    )

def describe_popularity(book):
    p = book['Popularity']
    if p > 200:
        return 'cultural touchstone and a'
    elif p > 100:
        return 'deeply oversold'
    elif p > 75:
        return 'very'     
    elif p > 50:
        return 'popular'
    elif p > 25:
        return 'fairly well known'
    elif p > 10:
        return 'known'
    else:
        return 'relatively unknown'

def calc_price(book):
    availability = random.randrange(1, max(5, book['Transcripts Sold']))
    multiplier = max(1, book['Popularity'] / 10) / availability
    price = book['Base Price'] / multiplier
    return math.ceil(price)

def describe_book(self, msg):
    global desc_box
    
    def transcript_text():
        if book['Transcript Started'] is True:
            return f"Continue \"{book['Title']}\" Transcript"
        else:
            return f"Transcribe \"{book['Title']}\""


    book = self.player['Library'][int(self.value)]
    button_text = transcript_text()
    
    self.text_div.desc_box.delete()
    self.text_div.desc_box = ut.new_div(
        self.text_div,
        ut.base_class_dark + 'col-span-1 row-start-2 '
    )
    self.text_div.desc_box.description = ut.new_div(
        self.text_div.desc_box,
        ut.base_class_dark + 'rounded-full bg-indigo-300 p-5 '
    )
    self.text_div.desc_box.description.text = set_book_text(book)
    
    self.text_div.desc_box.choose_book = ut.create_menu_button(
        self.text_div.desc_box,
        button_text,
        self.text_div.desc_box,
        start_transcription)

    desc_box = self.text_div.desc_box

    cb = self.text_div.desc_box.choose_book
    cb.book = book
    cb.desc = self.text_div.desc_box
    cb.desk = self.desk
    cb.player = self.player
    cb.header = self.header
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

    def increment_time(time, player=self.player, header=self.header):
        player['Time'] += datetime.timedelta(minutes=time)
        time_banner = header.time_banner
        time_banner.label.text = f'Time: {player["Time"]}'
    pass

    def refresh_stamina(time, player=self.player, header=self.header):
        stamina_used = time * player['Stamina Per Minute']
        if player['Stamina'] - stamina_used < 0:
            player['Fatigue'] += max(1, player['Fatigue'])
        player['Stamina'] -= stamina_used
        stamina_banner = header.stamina_banner
        stamina_banner.label.text = f'Stamina: {player["Stamina"]}'
    pass

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
            refresh_stamina(self.time)
            increment_time(self.time)
            transcription_info()
        pass

    def proofread_transcript(self, msg):
        skill_set = self.player['Skills']
        read_speed = skill_set['Base Read'] * skill_set['Read']
        self.time = math.ceil(self.book['Word Count'] / read_speed)
        self.book['Is Proofread'] = True
        refresh_stamina(self.time)
        increment_time(self.time)
        transcription_info()
        pass

    def correct_transcript(self, msg):
        
        pass

    def find_buyer(self, msg):

        def decrement_stamina(loss):
            self.player['Stamina'] -= max(loss * self.player['Fatigue'], 1)
            stamina_banner = self.header.stamina_banner
            stamina_banner.label.text = f'Stamina: {self.player["Stamina"]}'
            pass
        popularity_discount = random.randrange(self.book['Popularity'], 120)
        price_modifier = random.randrange(1, popularity_discount)
        price_in_cents = current_price * price_modifier
        transcript_price = math.ceil(price_in_cents / 100)
        increment_time(60)
        decrement_stamina(1)
        self.price.price = transcript_price
        self.price.label.text = f'Sell for {transcript_price}'

        pass

    def sell_work(self, msg):
        global desc_box
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
        
        print(desc_box.description.text)
        desc_box.description.text = set_book_text(self.book)
        transcription_info()
        pass

    def transcription_info():
        def basic_info():
            self.transcribe_area.title_line = ut.transcript_div(
                self.transcribe_area,
                f'Title: {self.book["Title"]}'
            )

            self.transcribe_area.word_count = ut.transcript_div(
                self.transcribe_area,
                f'Number of Words: {self.book["Word Count"]}'
            )

            self.transcribe_area.words_transcribed = ut.transcript_div(
                self.transcribe_area,
                f'Words Transcribed: {self.book["Words Transcribed"]}'
            )
            pass

        def allocate_supply_info():
            self.transcribe_area.supplies_needed = ut.transcript_div(
                self.transcribe_area,
                (
                    'Supplies needed: '
                    f'{supply_list()}'
                )
            )

            self.transcribe_area.can_allocate = ut.transcript_div(
                self.transcribe_area,
                f'{can_allocate()}'
            )

            if self.enough_supplies is True:
                self.transcribe_area.allocate_supplies = ut.create_button(
                    self.transcribe_area,
                    "Allocate Supplies",
                    allocate_supplies
                )
                a = self.transcribe_area.allocate_supplies
                a.player = self.player
                a.sheets = self.sheets
                a.ink = self.ink
                a.desk = self.desk
                a.book = self.book
            pass

        def transcript_progress():
            self.transcribe_area.words_transcribed = ut.transcript_div(
                self.transcribe_area,
                (
                    'Estimated Time to Complete: '
                    f'{time_estimate()} minutes'
                )
            )
            self.transcribe_area.time_picker = ut.transcript_div(
                self.transcribe_area,
                'Write for how many minutes?  '
            )
            self.transcribe_area.time_picker.input = ut.input_number(
                self.transcribe_area.time_picker,
                self.time_estimate,
                validate_input
                )

            self.transcribe_area.time_picker.transcribe = ut.create_button(
                self.transcribe_area,
                f'Write for {self.time_estimate} minutes',
                write_transcript
            )
            t = self.transcribe_area.time_picker.transcribe
            t.time = self.time_estimate
            t.player = self.player
            t.header = self.header
            t.desk = self.desk
            t.book = self.book
            t.estimate = self.time_estimate
            self.transcribe_area.time_picker.input.transcribe = t
            pass

        def proofread_info():
            def correct_and_sell():
                self.transcribe_area.error_count = ut.transcript_div(
                    self.transcribe_area,
                    (
                        f"Errors Found: "
                        f"{self.book['Errors']}"
                    )
                )
                self.transcribe_area.current_price = ut.transcript_div(
                    self.transcribe_area,
                    f"Current Top Price: {current_price}"
                )
                if self.book['Errors'] > 0 :
                    if self.player['Stamina'] > 0:
                        self.transcribe_area.correct = ut.create_button(
                            self.transcribe_area,
                            'Correct Transcript',
                            correct_transcript
                        )
                else:
                    self.transcribe_area.sell = ut.create_button(
                        self.transcribe_area,
                        'Find Buyer (1 hour)',
                        find_buyer
                    )
                    self.transcribe_area.price = ut.create_button(
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
                    p.book = self.book
                    p.desc = self.desc
                    p.player = self.player
                    p.header = self.header
                pass    

            self.transcribe_area.completed_transcript = ut.transcript_div(
                self.transcribe_area,
                "Transcription Complete"
            )
            if self.book['Is Proofread']:
                correct_and_sell()
            else:
                self.transcribe_area.proofread = ut.create_button(
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