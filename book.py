#import libtcod as tcod
import random
import markovify
import math

'''
All the markov models are in newline format
'''


def make_markov_model(file, state_size):
    with open(file) as f:
        gen = f.read()
    model = markovify.NewlineText(gen, state_size=state_size)
    model.compile()
    return model


def make_short_sentence(model, length, test_output=True):
    sentence = None
    while sentence is None:
        sentence = model.make_short_sentence(length, test_output=test_output)
    return sentence


def make_sentence(model, test_output=True):
    sentence = None
    while sentence is None:
        sentence = model.make_sentence(test_output=test_output)
    return sentence


def scramble_authors():
    author_generated_list = open('./authors_random', 'a')
    author_core = make_markov_model("./authors.core", 1)
    for i in range(20000):
        author_generated_list.write(make_sentence(author_core) + "\n")
    author_generated_list.close()
    pass


def initialize_models():
    models = {}
    models["genre"] = make_markov_model("./genres.list", 1)
    models["title"] = make_markov_model("./book_titles.list", 1)
    #scramble_authors()
    models["author"] = make_markov_model("./authors_random", 1)
    # best_title_model = make_markov_model("./bestseller_titles.list", 1)
    return models


#  book functions  # 
def create_book():
    word_count = gen_words()
    return {
        'Title': gen_title(),
        'Author': gen_author(),
        'Genre': gen_genre(),
        'Word Count': word_count,
        'Type': gen_type(word_count),
        'Familiarity': 0,
        'Popularity': 0,
        'Transcripts Sold': 0,
        'Transcript Started': False,
        'Transcript Reward': gen_transcript_price(word_count)
    }


def gen_title():
    return make_short_sentence(model["title"], 45).title()


def gen_manuscript_title():
    return make_sentence(model["title"])

# def gen_bs_title():
#   return make_short_sentence(best_title_model, 30)


def gen_genre():
    genre_array = make_sentence(model["genre"]).split()
    if "literature" in genre_array:
        genre_array.remove("literature")
    elif "story" in genre_array:
        genre_array.remove("story")
    return " ".join(genre_array).title()


def gen_words():
    return random.randrange(190, 1300)


def gen_type(num_words):
    structure = ""
    if num_words in range(0, 500):
        structure = "essay"
    elif num_words in range(501, 7500):
        structure = "short story"
    elif num_words in range(7501, 17500):
        structure = "novellette"
    elif num_words in range(17501, 40000):
        structure = "novella"
    else:
        structure = "novel"
    return structure


def gen_author():
    return make_short_sentence(model["author"], 30)


def gen_transcript_price(words):
    return math.floor(words / 100 * random.randrange(10, 30))


model = initialize_models()
