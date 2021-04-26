import random
import datetime
import book


def populate_library():
    library = []
    for i in range(10):
        library.append(book.create_book())
    return library



def new_player():
    return {
        'Name': book.gen_author(),
        'Job': "Aspiring Author",
        'Library': populate_library(),
        'Desk': {
            'Paper': 100,
            'Ink': 50,
            'Pen': {
                'Name': 'Good Pen',
                'Error Rate': 0.02,
                'WordsPerSheet': 200
            }
        },
        'Snacks': random.randrange(1, 10),
        'Money': random.randrange(20, 50),
        'Time': datetime.datetime(2000, 1, 1, 7, 0, 0),
        'Stamina': 100,
        'Lit Speed': 150,
        'Skills': {
            'Read': 2,
            'Write': 1
        }
    }
