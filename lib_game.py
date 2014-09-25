import lib
from lib import Lib

def play_game():
	display_intro()
	plyr_name = get_player_name()
	lib = Lib()
	request_words(lib)
	display_story(lib)
	if play_again():
		play_game()

def display_intro():
	print("Welcome to LIB, the fun game to learn parts of speech")

def get_player_name():
	return input("What is your name?: ")

def request_words(lib):
	print("Enter words that match each part of speech below: ")
	for phrase in lib.lib_xml.getiterator("phrase"):
		if phrase.attrib.get("speech_part") is not None:
			word = input(phrase.attrib.get("speech_part") + ": ")
			lib.set_word(phrase, word)

def display_story(lib):
	print(lib.construct_story())

def play_again():
	response = input("Do you want to try another LIB? (y/n):")
	if response.lower() == "y":
		play_game()
	elif response.lower() != "n":
		print("That is not a valid response.")
		play_again()

if __name__ == '__main__':
	play_game()