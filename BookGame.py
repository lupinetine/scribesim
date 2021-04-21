#import libtcod as tcod
import re, random
import book 
import justpy as jp


player = {
	'Name': None,
	'Library' : [], 
	'Desk': {
		'Paper' : 100, 
		'Ink' : 50, 
		'Pen': {
			'Name': 'Good Pen', 
			'Error Rate': 0.02, 
			'BWPS': 200
		}
	}, 
	'Dolaridoos' : 0, 
	'Stamina' : 100, 
	'Skills': {
		'Read': 2, 
		'Write': 1
	}
}

def buy_supplies(supply, quantity):
	print("Okay, going to the store and buying %s for a total of %s." % (supply, player['Desk'][supply]+quantity))
	player['Desk'][supply]+= quantity
	pass
	



def describe_book(book):
	print("*********")
	print("This %s is titled \"%s\". It is written by %s." % (book["Type"], book["Title"], book["Author"]))
	print("It is a popular work in the %s genre and consists of %s words." % (book["Genre"], book["Word Count"]))
	print("The price for completing the transcript is %s dollaridoos." % (book["Transcript Reward"]))
	print("*********\n")
	pass

def populate_library(library):
	for i in range(10):
		library.append(book.create_book())

def player_name_set(webpage):
	pass
	
	
def initialize_player():

	player['Name'] = player_name()
	print("Welcome %s!" % player['Name'])
	populate_library(player['Library'])	
	pass

def gamemenu():
    wp = jp.WebPage()
    some_design = "w-64 bg-blue-500 m-2 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
    welcome_button = jp.P(text=f'Welcome Traveller!',a=wp, classes=some_design)
    #welcome_button.on('click', player_name_set(wp) )
    return wp
	


#initialize_player()
jp.justpy(gamemenu)

#for i in player['Library']:
#	describe_book(i)

