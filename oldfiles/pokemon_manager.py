# Author: Noah Herrin
# Project: PokemonPY
# Purpose: Wrapper classes to simplify and maintain a standard for dictionaries
#          representing the data for each pokemon instance
import time
import json
class pokemon:
    def __init__(self,data):
        self.data = dict(data)
        if not 'name' in self.data: raise Exception("Invalid Data: {}".format(data))
        self.name = data["name"]
        self.moves = {}

    def secondary_init(self, level):
        self.data["level"] = level
    def add_move(self,name,data):
        self.moves[name] = dict(data)
    def print(self):
        print(self.data)
        print(self.moves)

class data_collection_manager:
    def __init__(self, pokemon_data, move_data):
        print("test5",json.dumps(move_data,indent=4))
        self.pokemon_master_copy = pokemon_data
        self.move_master_copy = dict(move_data)


    def fetch_pokemon_data(self, name):
        if name not in self.pokemon_master_copy: raise Exception("Invalid Arguement: {}".format(name))
        return self.pokemon_master_copy[name]
    def create_new_pokemon(self, name):
        if name not in self.pokemon_master_copy: raise Exception("Attempted To Create New Pokemon With Invalid Name: {}".format(name))
        return pokemon(self.pokemon_master_copy[name])
    def fetch_move(self, name):
        if name not in self.move_master_copy: raise Exception("Unable to fetch move {}".format(name))
        return self.move_master_copy[name]

def initialize(pokemon_data,move_data):
    print("testa",move_data)
    pm = pokemon_manager(pokemon_data,move_data)
    print(pm.fetch_pokemon_data("Charmander"))
    p1 = pm.create_new_pokemon("Squirtle")
    p1.secondary_init(6)
    #p1.add_move("Ember",pm.fetch_move("Ember"))
    p1.print()
