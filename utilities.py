import datetime
import book
import justpy as jp

# CLASSES CSS #
base_class = "text-white rounded text-center "
base_class_dark = "text-indigo rounded text-center "
input_class = "w-12 rounded text-indigo "
library_display_class = "grid grid-cols-3 divide-x bg-gray-300 col-span-auto "
grid_base = "grid auto-cols-4 "
button_base = "m-3 ring-4 ring-black-600 text-gray-50 font-bold rounded "
button_base_dark = "m-3 ring-4 ring-white-600 text-purple-800 font-bold rounded "
player_name = base_class + "m-1 font-black bg-indigo-500 "
header_base = base_class + "m-2 font-bold justify-center "
header_base_dark = base_class_dark + "m-2 font-bold justify-center "
button_menu = button_base + "bg-blue-600 p-2 inline "
food_menu = button_base + "bg-green-800 p-2 inline "


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

def update_stamina_banner(loss, header, player):
    player['Stamina'] -= loss
    header.stamina_banner.value.text = f'{player["Stamina"]}'
    header.stamina_banner.classes = stamina_header(player['Fatigue'])
    #header.stamina_banner.label.classes = stamina_header(player['Fatigue'])

def update_money_banner(change, header, player):
    player['Money'] -= change
    header.money_banner.value.text = f'{player["Money"]}'

def update_food_banner(header, player):
    header.food_banner.value.text = f'{len(player["Stocks"]["Food"])}'


def update_time(time, header, player):
    player['Time'] += datetime.timedelta(minutes=time)
    # print(player['Time'])
    # print(player['Time'].hour)
    header.time_banner.value.text = f'{player["Time"]}'


def stamina_header(fatigue):
    if fatigue > 20:
        return header_base + "bg-red-900 "
    elif fatigue > 15:
        return header_base + "bg-red-800 "
    elif fatigue > 10:
        return header_base + "bg-red-700 "
    elif fatigue > 5:
        return header_base + "bg-red-600 "
    elif fatigue > 3:
        return header_base + "bg-red-500 "
    elif fatigue > 2:
        return header_base + "bg-red-400 "
    else:
        return header_base_dark + "bg-red-300 "
    

def update_desk_banner(div, player):
    div.paper = desk_item(div, "Paper Tray", player['Desk']['Paper'])
    div.ink = desk_item(div, "Inkwell", player['Desk']['Ink'])
    div.pen = desk_item(div, "Pen Holder", player['Desk']['Pen'])
    

def input_number(div, max, change, classes=input_class):
    return jp.InputChangeOnly(
        type='number',
        min=0,
        max=max,
        a=div,
        change=change,
        classes=classes
    )

def populate_library():
    library = []
    for _ in range(5):
        library.append(book.create_book())
    return library

def new_name():
    return book.gen_author()

def new_webpage(): return jp.WebPage(delete_flag=True)

def run_game(entry): return jp.justpy(entry, host='0.0.0.0', port=8080)

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


def new_div(div, classes=base_class):
    return jp.Div(a=div, classes=classes)


def new_para(div, classes=base_class):
    return jp.P(a=div, classes=classes)


def text_div(div, text, classes=base_class):
    return jp.Div(a=div, text=text, classes=classes)


def transcript_div(main_div, text):
    div = jp.Div(a=main_div)
    div.text = text
    return div


def player_div_banner(stat, dict, div, classes):
    if stat == 'Food':
        value = len(dict[stat])
    else:
        value = dict[stat]
    new_div = jp.Div(
        a=div,
        classes=classes
    )
    new_div.label = jp.P(
        text=f'{stat}: ',
        a=new_div,
        classes=classes + "justify-self-center inline-block "
    )
    new_div.value = jp.P(
        text=f'{value}',
        a=new_div,
        classes=classes + "justify-self-center inline-block "
    )
    return new_div


def lib_select(div, change, classes):
    return jp.Select(
        a=div,
        change=change,
        classes=classes
    )


def lib_option(text, value, text_div):
    return jp.Option(
    text=text,
    value=value,
    text_div=text_div
)


def create_menu_button(div, text, click, display, classes=button_menu):
    button = create_button(div, text, click, classes)
    button.display = display
    return button


def create_button(div, text, click, classes=button_menu):
    button = create_empty_button(div, text, classes)
    button.on('click', click)
    return button


def create_empty_button(div, text, classes=button_menu):
    button = jp.Button(a=div, classes=classes)
    button.label = jp.P(a=button, text=text)
    return button