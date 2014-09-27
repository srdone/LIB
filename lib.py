#Object code for a lib and lib processing

import xml.etree.ElementTree as ET

class Lib:
	def __init__(self):
		self.lib_xml = open_lib_xml()

	def set_word(self, id, word):
		#retrieve the phrase element with a given id from the xml
		phrase = self.lib_xml.find(".//phrase[@id='" + id + "']")
		phrase.attrib["word"] = word

	def gen_speech_parts(self):
		for phrase in self.lib_xml.getiterator("phrase"):
			if phrase.get("speech_part") is not None:
				yield {"id": phrase.get("id"), "speech_part": phrase.get("speech_part")}

	def gen_story(self):
		for line in self.lib_xml.getiterator("phrase"):
			string = (line.attrib.get("text") if line.attrib.get("text") is not None else "")
			string = string + (line.attrib.get("word") if line.attrib.get("word") is not None else "")
			string = string + (line.attrib.get("tail") if line.attrib.get("tail") is not None else "")
			string = string + " "
			yield string

def open_lib_xml():
	filename = input("Enter the location of the lib file you want: ")
	with open(filename, "r") as lib_file:
		lib_xml = ET.parse(lib_file)
		return lib_xml