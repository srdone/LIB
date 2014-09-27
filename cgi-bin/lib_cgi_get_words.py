#! /usr/bin/env python3

import cgi, sys
import lib
from lib import Lib

sys.stderr = sys.stdout

form = cgi.FieldStorage()
print('Content-type: text/html\n') #parse form data
print('<title>Word Request</title>')
print('<body>')
if not 'libtitle' in form:
	print('<h1>You did not enter a lib name.</h1>')
else:
	print('<h1>Please enter words to match the given parts of speech</h1>')
	lib = Lib(form['libtitle'].value)
	print('<form method=POST action="cgi-bin/lib_cgi_display_story.py">')
	for phrase in lib.gen_speech_parts():
		print('<P><B>{} : <B><input type=text name={}>'.format(phrase['speech_part'], phrase['id']))
	print('<input type=hidden name=libtitle value={}'.format(form['libtitle'].value)) #pass the name of the lib we are working with
	print('<P><B><input type=submit></B>')
	print('</body>')