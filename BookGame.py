#import libtcod as tcod
import re, random
import markovify 
import book 

def describe_book(book):
	print("This %s is titled %s" % (book["Type"], book["Title"])) 
	pass

for i in range(10):
	new_book = book.create_book()
	for k, v in new_book.items():
		print("%s : %s" % (k,v))
	print("***********")
	#print(book.gen_author())
	#print(make_sentence(genre_model))