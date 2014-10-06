#! /usr/bin/env python3

import cgi, sys
import lib
from lib import Lib
import cgitb
cgitb.enable()

sys.stderr = sys.stdout

form = cgi.FieldStorage()

#recreate the lib we are working with
lib = Lib('../lib_data/' + form['libtitle'].value + '.xml')

#set the words in the lib from previous page
for key in form.keys():
	if key != 'libtitle':
		lib.set_word(key, form[key].value)

def create_story_string():
	'Creates a string containing the full lib story'
	string = ""
	for phrase in lib.gen_story(line_ending='<br>'):
		string = string + phrase
	return string

'Writes the opening text of the webpage.'
print('Content-type: text/html\n') #parse form data
print('<title>Final Story</title>')
print('<body>')


'''Generates the body of the webpage, recreating the story
with the words selected on the previous page.'''
print('<h1>Your Story</h1>')

print('<P>')
print(create_story_string())
print('</P>')

'Writes the closing text of the webpage.'
print('</body>')