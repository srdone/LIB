#! /usr/bin/env python3

import cgi
import lib
from lib import Lib

form = cgi.FieldStorage()

#recreate the lib we are working with
lib = Lib(form['libtitle'].value)

#set the words in the lib from previous page
for field in form:
	lib.set_word(field.key, field.value)

print('Content-type: text/html\n') #parse form data
print('<title>Final Story</title>')
print('<body>')

print('<h1>Your Story</h1>')

for phrase in lib.gen_story():
	print('<P>' + phrase)

print('</body>')