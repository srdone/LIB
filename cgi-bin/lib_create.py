#! /usr/bin/env python3

import cgi, sys
import lib
from lib import Lib

#show std errors in the console
sys.stderr = sys.stdout

#get data from the previous page
form = cgi.FieldStorage()

#create blank lib
lib = Lib()



##Begin webpage
print('Content-type: text/html\n') #parse form data
print('<title>Built Lib</title>')
print('<body>')

#Fill lib in with data from cgi form
n = 0
while n < 2:			#(length(form)/4):
	line_attributes = {}
	line_attributes['text'] = form[('text' + str(n))].value
	line_attributes['speech-part'] = form.getvalue('speech-part' + str(n))
	line_attributes['tail'] = form.getvalue('tail' + str(n))
	line_attributes['paragraph'] = form.getvalue('paragraph' + str(n))
	lib.add_phrase(n, line_attributes)
	n = n + 1

#build and print story
string = ""
for phrase in lib.gen_story(line_ending='<br>'):
	string = string + phrase
	print(string)
print(string)

#close page
print('</body>')