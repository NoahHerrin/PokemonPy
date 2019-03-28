# events to implement
# battling
# game: you encounter a wild pokemon
# game: you sent out your pokemon
# game: what would you like to do
# game: [attack][bag][party][run]
# input: attack
# game: which move would you like to use
# game: [pound][scratch][flamethrower][leer]
# input: pound
# game: you used pound it was very effective
# game: pokemon used flamethrower it wasn't very effective
# game: what would you like to do
# using item
class battle:
    def __init__(self, player, other, is_trainer_battle):
        if is is_trainer_battle:
            self.mode = "battle"
        else:
            self.mode = "encounter"

        self.player = player
        self.other = other # self.mode will determine if we treat other as player object or as pokemon objects

    def prompt_option(self):
        print("What would you like to do?\n[Fight][Bag][Party][Run]")

    def prompt_move(self):
        #example printing same moves every time
        pass
