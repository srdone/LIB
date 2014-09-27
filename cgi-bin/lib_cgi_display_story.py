#! /usr/bin/env python3

import cgi, sys
import lib
from lib import Lib
import cgitb
cgitb.enable()

sys.stderr = sys.stdout

form = cgi.FieldStorage()

#recreate the lib we are working with
lib = Lib(form['libtitle'].value)

#set the words in the lib from previous page
for key in form.keys():
	if key != 'libtitle':
		lib.set_word(key, form[key].value)

print('Content-type: text/html\n') #parse form data
print('<title>Final Story</title>')
print('<body>')

print('<h1>Your Story</h1>')

for phrase in lib.gen_story():
	print('<P>' + phrase)

print('</body>')