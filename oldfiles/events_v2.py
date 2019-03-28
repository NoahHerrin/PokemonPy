
# Author: Noah Herrin
# Project: PokemonPY
# Purpose: Contains the code for the basic events that a player will encounter
#
#
class pokemon_battle:
    def __init__(self, pokemon, npc):
        self.pokemon = pokemon      # pokemon controlled by player
        self.npc = npc              # pokemon controlled by computer
        self.is_player_turn = True  # later make this a result of somecalculation using speed stats
    def player_turn(self):
        # player can either
        #   - attack
        #   - heal
        #   - swap pokemon
        #   - run
        # fetch input
        input = "attack"
        move =
        pass

    def use_attack(self):
        # print available moves
        # check which move they enter
        # deal appropriate damage to npc
        print(self.pokemon.moves_to_string())
        current_move = self.npc.fetch_random_move()
        remaining_health = self.pokemon.take_damage(self.npc.fetch_move(current_move))
        print("{} has {} health remaining".format(self.npc.stats['name'],remaining_health))

    def process_attack(self, move_name):
        if self.is_player_turn: # player attacking npc
            remaining_health = self.npc.take_damage(self.player.fetch_move(current_move))
            print("{} has {} health remaining".format(self.npc.stats['name'],remaining_health))
        else: # npc attacking player
    def npc_turn(self):
        # assume it's a wild pokemon
        #   - attack
        #   - run away [1% chance per turn]* except legendaries
        current_move = self.npc.fetch_random_move()
        remaining_health = self.pokemon.take_damage(self.npc.fetch_move(current_move))
        print("{} has {} health remaining".format(self.npc.stats['name'],remaining_health))
    def take_turn(self):
        if is_player_turn:
            self.player_turn()
        else:
            self.npc_turn()
