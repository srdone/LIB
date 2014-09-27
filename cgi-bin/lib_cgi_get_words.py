#! /usr/bin/env python3

import cgi
import lib
from lib import Lib

form = cgi.FieldStorage()
print('Content-type: text/html\n') #parse form data
print('<title>Word Request</title>')
print('<body>')
if not 'libtitle' in form:
	print('<h1>You did not enter a lib name.</h1>')
else:
	print('<h1>Please enter words to match the given parts of speech</h1>')
	lib = Lib(form['libtitle'].value)
	print(<form method=POST action="cgi-bin/lib_cgi_display_story.py">)
	for phrase in lib.gen_speech_parts():
		print('<P><B>{} : <B><input type=text name={}>'.format(phrase['speech-part'], phrase['id']))
	print('<P><B><input type=submit></B>')
	print('</body>')