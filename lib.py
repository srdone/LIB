#Object code for a lib and lib processing

import xml.etree.ElementTree as ET

class Lib:
	def __init__(self):
		self.lib_xml = open_lib_xml()

	def set_word(self, lib_line, word):
		lib_line.attrib["word"] = word

	def construct_story(self):
		#construct an iterator so other methods can display it how they like.
		string = ""
		for line in self.lib_xml.getiterator("phrase"):
			string = string + (line.attrib.get("text") if line.attrib.get("text") is not None else "")
			string = string + (line.attrib.get("word") if line.attrib.get("word") is not None else "")
			string = string + (line.attrib.get("tail") if line.attrib.get("tail") is not None else "")
			string = string + " "
		return string

def open_lib_xml():
	filename = input("Enter the location of the lib file you want: ")
	with open(filename, "r") as lib_file:
		lib_xml = ET.parse(lib_file)
		return lib_xml