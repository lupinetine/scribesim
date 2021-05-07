import random
import datetime
import book


def populate_library():
    library = []
    for i in range(5):
        library.append(book.create_book())
    return library


def new_player():
    return {
        'Name': book.gen_author(),
        'Job': "Aspiring Author",
        'Library': populate_library(),
        'Desk': {
            'Paper': {
                'Name': 'Standard Paper',
                'Sheets': 100
            },
            'Ink': {
                'Name': 'Black Ink',
                'Words Per ml': 400,
                'Milliliters': 50
            },
            'Pen': {
                'Name': 'Good Pen',
                'Error Rate': 0.02,
                'Words Per Sheet': 200
            }
        },
        'Snacks': random.randrange(4, 10),
        'Money': random.randrange(20, 50),
        'Time': datetime.datetime(2000, 1, 1, 7, 0, 0),
        'Stamina': 100,
        'Skills': {
            'Base Read': 150,  # in words per minute
            'Base Write': 20,  # in words per minute
            'Read': 2,
            'Write': 1
        }
    }
