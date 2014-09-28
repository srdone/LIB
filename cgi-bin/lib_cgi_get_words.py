#! /usr/bin/env python3

import cgi, sys
import lib
from lib import Lib

#show errors in the console
sys.stderr = sys.stdout

#get data from the previous page
form = cgi.FieldStorage()

def build_page():
	'Builds the components of the page'
	opening_text()
	#choose between two pages based on whether a form was filled out.
	if not 'libtitle' in form:
		no_lib()
	else:
		lib_chosen()
	closing_text()

def opening_text():
	'Writes the opening text of the page'
	print('Content-type: text/html\n') #parse form data
	print('<title>Word Request</title>')
	print('<body>')

def no_lib():
	'Print the page as it should appear if the user did not select a lib'
	print('<h1>You did not enter a lib name.</h1>')

def lib_chosen():
	'Writes the body of the page, containing the word parts and text boxes for the LIB'
	print('<h1>Please enter words to match the given parts of speech</h1>')
	lib = Lib('cgi-bin/lib_data/' + form['libtitle'].value + '.xml')
	print('<form method=POST action="cgi-bin/lib_cgi_display_story.py">')
	for phrase in lib.gen_speech_parts():
		print('<P><B>{} : <B><input type=text name={}></P>'.format(phrase['speech_part'], phrase['id']))
	print('<input type=hidden name=libtitle value={}'.format(form['libtitle'].value)) #pass the name of the lib we are working with
	print('<P><B><input type=submit></B></P>')

def closing_text():
	'Writes the closing text of the webpage'
	print('</body>')

if __name__ == '__main__':
	build_page()