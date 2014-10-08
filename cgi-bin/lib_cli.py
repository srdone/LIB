import lib as L
from lib import Lib

lib_directory = "../lib_data/"

def play_game():
	'Game flow'
	display_intro()
	plyr_name = get_player_name()
	lib = L.open_lib_file(get_lib_name())
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
	lib_file_name = input("Enter the relative path to your lib file.")
	return (lib_directory + lib_file_name)

def request_words(lib):
	'''Ask the user to pick a word for each speech part in the Lib.
	Set the word in the lib using the id of the speech_part.'''
	print("Enter words that match each part of speech below: ")
	for speech_part in lib.gen_speech_parts():
		word = input(speech_part["speech_part"] + ": ")
		lib.set_word(speech_part["id"], word)

def display_story(lib):
	'Displays the story, consisting of the filled in phrases.'
	story = ""
	for phrase in lib.gen_story():
		story = story + phrase
	print(story)

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