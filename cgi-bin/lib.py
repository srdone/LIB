#Object code for a lib and lib processing

import xml.etree.ElementTree as ET

class Lib:
	def __init__(self, filename=None):
		'''Takes an xml filename and processes it to allow a Lib
		to be generated and interacted with.'''
		if filename:
			self.lib_xml = open_lib_xml(filename)
		else:
			self.lib_xml = ET.Element('data')

	def set_word(self, id, word):
		'''Retrieve the phrase element with a given id from the xml
		and assign a new attribute for the selected word to match the speech_part'''
		phrase = self.lib_xml.find(".//phrase[@id='" + id + "']")
		phrase.attrib["word"] = word

	def gen_speech_parts(self):
		'''A generator that gives each speech_part and the id of the phrase it belongs to.'''
		for phrase in self.lib_xml.getiterator("phrase"):
			if phrase.get("speech_part") is not None:
				yield {"id": phrase.get("id"), "speech_part": phrase.get("speech_part")}

	def gen_story(self, line_ending='\n'):
		'''A generator that constructs a string for each phrase.
		Assumes that a word attribute has been selected.'''
		for line in self.lib_xml.getiterator("phrase"):
			string = (line.attrib.get("text") if line.attrib.get("text") is not None else "")
			if line.attrib.get("word"):
				string = string + (line.attrib.get("word") if line.attrib.get("word") is not None else "")
			else:
				string = string + (line.attrib.get("speech_part") if line.attrib.get("speech_part") is not None else "")
			string = string + (line.attrib.get("tail") if line.attrib.get("tail") is not None else "")
			string = (string + line_ending if line.attrib.get('paragraph')=='true' else string) #Create new line if needed.
			yield string

	def add_phrase(self, id, attributes):
		'''
		Adds a phrase to the lib.
		'''
		line = ET.SubElement(self.lib_xml, "phrase")
		for key in attributes.keys():
			line.set(key, attributes[key])

def open_lib_xml(filename):
	'''Opens an xml file and returns the parsed xml.'''
	with open(filename, "r") as lib_file:
		lib_xml = ET.parse(lib_file)
		return lib_xml

def list_available_libs():
	pass