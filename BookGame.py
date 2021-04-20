#import libtcod as tcod
import re, random
import markovify 
import book 

library = []


def describe_book(book):
	print("*********")
	print("This %s is titled \"%s\". It is written by %s." % (book["Type"], book["Title"], book["Author"]))
	print("It is a popular work in the %s genre and consists of %s words." % (book["Genre"], book["Word Count"]))
	print("The price for completing the transaction is %s dolaridoos." % (book["Transcript Reward"]))
	print("*********")
	pass

def populate_library(library):
	for i in range(10):
		library.append(book.create_book())

populate_library(library)
for i in library:
	describe_book(i)