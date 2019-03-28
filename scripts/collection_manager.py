# Author: Noah Herrin
# Project: PokemonPY
# Purpose: to create a reusable and extensible data structure for handling catagories
#          of game data. Example: pokemon, moves, and items
#
#
import json

class collection:
    def __init__(self, title,data):
        self.title = title
        self.master_copy = data.copy()

    # given an unused key will create a new entry in collection
    def add_entry(self, key, value):
        if key in self.master_copy: raise Exception("Key Already Exists: {}".format(key))
        self.master_copy[key] = value
    # modifies entry or value within an entry
    def modify_entry(self, key_1, key_2, new_value=None):
        # validate parameters
        if key_1 not in self.master_copy: raise Exception("Invalid Key: {}".format(key_1))
        #check if we are modifying entire entry or value in an add_entry
        if new_value == None:
            self.master_copy[key_1] = key_2
        elif key2 in self.master_copy:
            self.master_copy[key_1][key_2] = new_value
        else:
            raise Exception("Invalid Key2: {}".format(key_2))

    # takes a key to an existing entry and returns the value
    def fetch_entry(self, key):
        if key not in self.master_copy: raise Exception("Invalid Key: {}".format(key))
        return self.master_copy[key].copy()

    # returns a json representation of collection
    def toString(self):
        return json.dumps(self.master_copy, indent=4)

def create_collection(label,data):
    return collection(label,data)
