# Object code for a lib and lib processing

import xml.etree.ElementTree as ET
import json
import os.path

class Lib:
    def __init__(self, lib_location = None):
        self.lib_data = []
        if lib_location is not None:
            open_lib_file

    def set_word(self, phrase_id, word):
        for phrase in self.lib_data:
            if phrase["id"] == phrase_id:
                phrase["word"] = word
                break

    def gen_speech_parts(self):
        '''A generator that gives each speech_part and the id of the phrase it belongs to.'''
        for phrase in sorted(self.lib_data, key=lambda phrase: phrase["id"]):
            if "speech_part" in phrase:
                yield {"id": phrase["id"], "speech_part": phrase["speech_part"]}

    def gen_story(self, phrase_ending='\n'):
        '''A generator that constructs a string for each phrase.
        Assumes that a word attribute has been selected.'''
        for phrase in sorted(self.lib_data, key=lambda phrase: phrase["id"]):
            string = (phrase["text"] if phrase["text"] is not None else "")
            if phrase["word"]:
                string = string + (phrase["word"] if phrase["word"] is not None else "")
            else:
                string = string + (phrase["speech_part"] if phrase["speech_part"] is not None else "")
            string = string + (phrase["tail"] if phrase["tail"] is not None else "")
            string = (string + phrase_ending if phrase['paragraph'] == True else string)  #Create new phrase if needed.
            yield string

    def add_phrase(self, id, attributes):
        '''Adds a phrase to the lib.'''
        phrase = {}
        for key in attributes.keys():
            phrase[key] = attributes[key]
        phrase["id"] = id
        self.lib_data.append(phrase)

def open_lib_file(filename):
    '''Opens an xml or json file and parses it to create a lib object.'''
    with open(filename, "r") as lib_file:
        extension = os.path.splitext(filename)[1]
        if extension == '.xml':
            return create_lib_from_xml(lib_file)
        elif extension == '.json':
            return create_lib_from_json(lib_file)

def create_lib_from_xml(lib_file):
    "parses xml to create a lib object"
    lib = Lib()
    tree = ET.parse(lib_file)
    root = tree.getroot()
    for phrase in root.findall('phrase'):
        parsed_phrase = {}
        parsed_phrase["text"] = phrase.get("text")
        parsed_phrase["word"] = (phrase.get("word") if phrase.get("word") is not None else "")
        parsed_phrase["speech_part"] = phrase.get('speech_part')
        parsed_phrase["tail"] = phrase.get("tail")
        parsed_phrase["paragraph"] = True if phrase.get("paragraph") == "true" else False
        lib.add_phrase(int(phrase.get("id")), parsed_phrase)
    return lib

def create_lib_from_json(lib_file):
    "parses json to create a lib object"
    lib = Lib()
    lib_json = json.loads(lib_file.read())
    for phrase in lib_json["phrases"]:
        parsed_phrase = {}
        parsed_phrase["text"] = phrase["text"]
        parsed_phrase["word"] = (phrase["word"] if "word" in phrase else "")
        parsed_phrase["speech_part"] = phrase['speech_part']
        parsed_phrase["tail"] = phrase["tail"]
        parsed_phrase["paragraph"] = phrase["paragraph"]
        lib.add_phrase(phrase["id"], parsed_phrase)
    return lib