# Author: Noah Herrin
# Project: PokemonPY
# Purpose: I am creating a text based pokemon game to motivate myself to learn more about
#          the python programming language and it's libraries
# To Do List:
#   + create object oriented structure for pokemon objects
#       + pokemon data stored in spreadsheet for maximum extensibility
#       + pokemon move data stored in spreadsheet for maximum extensibility
#       + ability to toggle when data is uploaded from spreadsheets
#   - create interaction object (manual no input yet)
#       - wild pokemon encounter interaction
#       - wild pokemon battles
#       - trainer pokemon battles
#   - implement command line controls for interactions
#
import sys
import time
sys.path.insert(0,"D:\Documents\Projects\PyPokemon\scripts")
import resource_loader as loader
import collection_manager as collections
import test_timer as test_timer
import json
import pokemon as pokemon_manager
import events as events





#create_collection("pokemon",loader_data[2])
#create_collection("moves",loader_data[1])
def initialize_data():
    resources = {
        "pokemon" :"PokemonData.xlsx",
        "moves" : "MoveData.xlsx",
        "items" : "ItemData.xlsx"
    }
    loader_data = loader.load_data(resources)
    #for index in range(len(loader_data)): print(json.dumps(loader_data[index],indent=4))
    i = 0
    for key in resources:
        resources[key] = {
        'file-name': resources,
        'collection': collections.create_collection(key, loader_data[i] )
        }
        i += 1
    return resources
def main():
    # contains copies of various objects at their initial state
    master_copy = initialize_data()
    #print(json.dumps(master_copy['pokemon']['collection'].fetch_entry("Charmander")))

    copy = pokemon_manager.create_pokemon(master_copy['pokemon']['collection'].fetch_entry("Charmander"))
    copy.init_stats(8)
    copy.add_move("Flamethrower",master_copy['moves']['collection'].fetch_entry('Flamethrower'))
    copy.add_move("Pound",master_copy['moves']['collection'].fetch_entry('Pound'))
    moves = ["Flamethrower","Pound","Ember"]
    move_data = {}
    for str in moves:
        move_data[str] = master_copy['moves']['collection'].fetch_entry(str)
    events.use_attack("Charizard",move_data)
    #print(copy.get_move_damage("Flamethrower"))
    #print(copy.get_move_damage("Pound"))
    #print(copy.moves_to_string())

main()
