import tool_kit as tools
# Author: Noah Herrin
# Project: PokemonPY
# Purpose: establish a standard for handling various events in the game, by
#          creating classes to standardize the handling of each type of event.
#          create reusable and versitile functions to ensure consistancy in
#          different event types
#
# Battle/Pokemon encounter's simplified
#   1. Opponent requires introduction
#       ex. "You have encountered a wild x" or "Trainer x has challenged you"
#   2. Start default player process
#       ex use whatever pokemon is in position 1 in your party and introduce them
#   3. Display encounter options
#       can be any of the following
#           fight
#           bag
#           run
#           party
#   4. user chooses an option which should then prompt them with the sum options
#       fight
#           display moves
#           ask which move they would like to use
#       bag
#           display items
#           ask which item they would like to use
#           each item will behave differently but once it has been selected
#           it does not require any input from the player
#               could standardize throw pokeball function
#               could standardize use heal
#               could standardize use effect clearing item
#       run
#           display message
#           exit event
#       party
#           display pokemon in party
#           ask which pokemon they would like to swap to
#           swap active pokemon
#       * in every option but run, player is prompted and then asked for input
#         this seems like it could be made into one class or function
#  5. Repeat steps 3-4 until player runs out of pokemon, runs, defeats opponents
#     pokemon or catches pokemon
#  6. Check if pokemon has leveled up or player recieved any gifts

def introduce_pokemon(pokemon_name, shiny=False, trainer_name=None):
    if trainer_name is None:
        if shiny:
            print("You have encountered a wild shiny {}!".format(pokemon_name))
        else:
            print("You have encountered a wild {}!".format(pokemon_name))
    else:
        print("{} sent out {}!".format(trainer_name, pokemon_name))
def use_attack(pokemon_name, moves):
    # print out moves
    # move_name [type] damage x/total pp
    # ex flamethrower [fire] 100 dmg
    # or pound [normal/fighting] 100 dmg
    for key, value in moves.items():

        print("[[{}] {}]".format(value['type'], tools.add_padding_left(key, 20 -len(value['type']))))
class battle:
    def __init__(self, player, other, is_trainer_battle):
        if is_trainer_battle:
            self.mode = "battle"
        else:
            self.mode = "encounter"
        self.player = player
        self.other  = other # either the other player or pokemon,


    def get_options(self):

        options = "What would you like to do?\n[Fight][Bag][Party]"
        if self.mode is "encounter":
            options += "[Run]"
        return options
