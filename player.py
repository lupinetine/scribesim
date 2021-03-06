import random
import datetime
import utilities as ut

def new_player():
    return {
        'Name': ut.new_name(),
        'Job': "Aspiring Author",
        'Library': ut.populate_library(),
        'Desk': {
            'Paper': {
                'Name': 'Standard Paper',
                'Sheets': 100
            },
            'Ink': {
                'Name': 'Black Ink',
                'Milliliters': 50
            },
            'Pen': {
                'Name': 'Good Pen',
                'Error Rate': 0.02,
                'Words Per ml': 400,
                'Words Per Sheet': 200
            }
        },
        'Stocks': {
            'Paper': [],
            'Ink': [],
            'Pen': [],
            'Food': []
        },
        'Money': random.randrange(20, 50),
        'Time': datetime.datetime(2000, 1, 1, 7, 0, 0),
        'Stamina': 100,
        'Stamina Per Minute': 0.5,
        'Fatigue': 0,
        'Skills': {
            'Base Read': 150,  # in words per minute
            'Base Write': 20,  # in words per minute
            'Read': 2,
            'Write': 1
        }
    }
