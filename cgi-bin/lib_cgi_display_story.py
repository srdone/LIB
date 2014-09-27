#! /usr/bin/env python3

import cgi
import lib
from lib import Lib

form = cgi.FieldStorage()

#Need to figure out how to get the lib from the previous cgi

print('Content-type: text/html\n') #parse form data
print('<title>Final Story</title>')
print('<body>')
for field in form:
	lib.set_word(field.key, field.value)
print('<h1>Your Story</h1>')

for phrase in lib.gen_story():
	print('<P>' + phrase)

print('</body>')