import lib
from lib import Lib

def play_game():
	'Game flow'
	display_intro()
	plyr_name = get_player_name()
	lib = Lib(get_lib_name())
	request_words(lib)
	display_story(lib)
	if play_again():
		play_game()

def display_intro():
	'''Displays the game introduction text.'''
	print("Welcome to LIB, the fun game to learn parts of speech")
	print("By entering words to match parst of speech, you produce a wacky story.")

def get_player_name():
	'Requests the name of the player.'
	return input("What is your name?: ")

def get_lib_name():
	'''Get the name and relative path of the Lib you want to play.'''
	return input("Enter the relative path to your lib file.")

def request_words(lib):
	'Ask the user to pick a word for each speech part in the Lib.'
	print("Enter words that match each part of speech below: ")
	for speech_part in lib.gen_speech_parts():
		word = input(speech_part["speech_part"] + ": ")
		lib.set_word(speech_part["id"], word)

def display_story(lib):
	'Displays the filled in phrases, one on each line.'
	for phrase in lib.gen_story():
		print(phrase)

def play_again():
	'Ask the player if they want to play again.'
	response = input("Do you want to try another LIB? (y/n):")
	if response.lower() == "y":
		play_game()
	elif response.lower() != "n":
		print("That is not a valid response.")
		play_again()

if __name__ == '__main__':
	play_game()