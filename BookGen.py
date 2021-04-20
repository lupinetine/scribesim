#import libtcod as tcod
import re, random
import markovify 

def make_markov_model(file, state_size):
	with open(file) as f:
		gen = f.read()
	return 	markovify.NewlineText(gen, state_size=state_size)

#### book functions ####
books_in_the_world = {}
def list_books():
	for i in books_in_the_world:
		print(i)
	pass

def create_books():

def gen_title():
	return make_short_sentence(title_model, 25)

def gen_manuscript_title():
	return make_sentence(title_model)

def gen_bs_title():
	return make_short_sentence(best_title_model, 30)

def gen_genre():
	genre_array = make_sentence(genre_model).split()
	if "literature" in genre_array:
		genre_array.remove("literature")
	elif "story" in genre_array:	
		genre_array.remove("story")
	return " ".join(genre_array)

def gen_words():
	return random.randrange(90, 300)

def gen_type(num_words):
	structure = ""
	if num_words in range(0,500):
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
	return make_short_sentence(author_model, 30)
	
def make_short_sentence(model, length, test_output=True):
	sentence = None
	while sentence == None:
		sentence = model.make_short_sentence(length, test_output=test_output)
	return sentence
	
def make_sentence(model, test_output=True):
	sentence = None
	while sentence == None:
		sentence = model.make_sentence(test_output=test_output)
	return sentence

def scramble_authors():
	author_generated_list = open('./authors_random', 'w')
	for i in range(20000):
		author_generated_list.write(make_sentence(author_model)+"\n")
	author_generated_list.close()
	pass

author_model_core = make_markov_model("./authors.core", 1)
genre_model = make_markov_model("./genres.list", 1)
title_model = make_markov_model("./book_titles.list", 1) 

best_title_model = make_markov_model("./bestseller_titles.list", 1)
author_model = make_markov_model("./authors_random", 1)

for i in range(20):
	print(gen_author())
	#print(make_sentence(genre_model))