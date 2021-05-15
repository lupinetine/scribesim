import justpy as jp

# CLASSES CSS #
base_class = "text-white rounded text-center "
base_class_dark = "text-indigo rounded text-center "
input_class = "w-12 rounded text-indigo "
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

def input_number(div, max, change, classes=input_class):
    return jp.InputChangeOnly(
        type='number',
        min=0,
        max=max,
        a=div,
        change=change,
        classes=classes
    )


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


def transcript_div(main_div, text):
    div = jp.Div(a=main_div)
    div.text = text
    return div


def player_div_banner(stat, div, classes, player):
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