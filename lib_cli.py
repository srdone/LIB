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

#Ask the user to pick a word for each speech part in the LIB
def request_words(lib):
	print("Enter words that match each part of speech below: ")
	for speech_part in lib.gen_speech_parts():
		word = input(speech_part["speech_part"] + ": ")
		lib.set_word(speech_part["id"], word)

def display_story(lib):
	for phrase in lib.gen_story():
		print(phrase)

def play_again():
	response = input("Do you want to try another LIB? (y/n):")
	if response.lower() == "y":
		play_game()
	elif response.lower() != "n":
		print("That is not a valid response.")
		play_again()

if __name__ == '__main__':
	play_game()