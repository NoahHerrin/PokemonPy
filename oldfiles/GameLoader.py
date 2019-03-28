from Pokemon import PokemonType
from Pokemon import Pokemon
from Pokemon import Pokedex
import os

class Loader:
    # takes a single string parameter which is a path to a file containing
    # data for each pokemontype
    def __init__(self):
        pass

    def validatePath(self, path):
        exists = os.path.isfile(path)
        if exists:
            return True
        else:
            return False

    def loadPokemonData(self,path):
        if self.validatePath(path):

            pokedex = Pokedex()
            file = open(path, "r")
            line = file.readline()
            print(len(file))
            # read data from file until end of file marker

            while not line == ":END:\n":
                # confirm that format is correct
                if not "Name: " in line:

                    raise Exception("Invalid Data Formating from {} given {}".format(path, line))
                else:

                    name = line.split("Name: ")[1].split()
                    line = file.readline().split
                    stats = {}
                    # add all stats in file to dictionary

                    while not ("Name: " in line or ":END:\n" in line):

                        print(line)
                        curStat = line.split(": ")
                        # validate format for pokemon stat

                        if len(curStat) == 2:
                            stats[curStat[0]] = curStat[1]
                        else:
                            raise Exception("Invalid Stat format. {}".format(curStat))
                        line = file.readline()
                print(stats)
            pokedex.addPokemon(name, stats)

        else:
            raise Exception("Invalid Path to Pokemon Data: {}".format(path))
