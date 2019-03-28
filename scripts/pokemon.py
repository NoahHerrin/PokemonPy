# Author: Noah Herrin
# Project: PokemonPY
# Purpose: Code associated with pokemon and their various interactions
import random
import json
class pokemon:
    def __init__(self, type_data):
        self.stats = type_data
        self.moves = {}
    # generates pokemon stats as a function of tier
    def init_stats(self, tier,level=1):
        # tier should be between 1 and 100
        if tier > 100 or tier < 0: raise Exception("Invalid Tier: {}".format(tier))
        # stats should be be between 0 (bad) and 10(exceptional)
        self.stats['health']  = self.calculate_stat(tier)
        self.stats['attack']  = self.calculate_stat(tier)
        self.stats['defence'] = self.calculate_stat(tier)
        self.stats['speed']   = self.calculate_stat(tier)
        self.stats['tier']    = tier
        self.stats['level']   = level

    def calculate_stat(self, tier):
        # calculate range (max 2 above tier, min 2 below tier)
        range = (tier / 4) * random.random() # stat will be [tier - range < stat < tier + range]

        if random.random() >= .5: # determine weather stat will be below or above the average
            range = range * -1
        if (tier + range) > 10: return 10
        if (tier + range) < 0: return 1
        return round(tier + range,2)

    def add_move(self, name, data):
        self.moves[name] = data
    def fetch_random_move(self):
        return random.choice(list(self.moves.keys()))
    def get_move_damage(self, name):
        # in the future request a type parameter to calculate bonus damage(example fire vs grass or water vs fire)
        damage = self.moves[name]['damage']
        return damage
    def fetch_move(self,name):
        return self.move[name]
    def take_damage(self, move_recieved):
        self.stats['health'] -= move_recieved['damage']
        return self.stats['health']

    def stats_to_string(self):
        return json.dumps(self.stats,indent=4)
    def moves_to_string(self):
        return json.dumps(self.moves,indent=4)
def create_pokemon(master_data):
    return pokemon(master_data)
