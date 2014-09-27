#! /usr/bin/env python3

import cgi, sys
import lib
from lib import Lib
import cgitb
cgitb.enable()

sys.stderr = sys.stdout

form = cgi.FieldStorage()

#recreate the lib we are working with
lib = Lib(form['libtitle'].value + '.xml')

#set the words in the lib from previous page
for key in form.keys():
	if key != 'libtitle':
		lib.set_word(key, form[key].value)

def build_page():
	opening_text()
	generate_body()
	closing_text()

def opening_text():
	'Writes the opening text of a webpage.'
	print('Content-type: text/html\n') #parse form data
	print('<title>Final Story</title>')
	print('<body>')

def generate_body():
	'''Generates the body of the webpage, recreating the story
	with the words selected on the previous page.'''
	print('<h1>Your Story</h1>')

	print('<P>')
	story = create_story_string()
	print_story(story)
	print('</P>')

def closing_text():
	'Writes the closing text of a webpage.'
	print('</body>')

def create_story_string():
	string = ""
	for phrase in lib.gen_story(line_ending='<br>'):
		string = string + phrase
	return string

def print_story(story):
	print('<P>' + story + '</P>')

if __name__ == '__main__':
	build_page()