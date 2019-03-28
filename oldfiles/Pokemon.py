#
class PokemonType:
    def __init__(self, id, name):
        self.Id = id
        self.Name = name
        self.Stats = {}

    def addStat(self, statName, statValue):
        # Check if stat already exists
        if statName in self.Stats:
            self.Stats[statName] = statValue
            return True
        else:
            return False

    def getStat(self, statName):
        # check if pokemon type has stat
        if statName in self.Stats:
            return self.Stats[statName]
        else:
            return False

    def getId(self):
        return self.Id
    def getName(self):
        return self.Name
    def printSimple(self):
        print("{} | {}".format(self.Id,self.Name))
    def printDetails(self):
        self.printSimple()
        for key,value in self.Stats.items():
            print("    {}: {}".format(key, value))
class Pokemon:
    def __init__(self, pokemonType):
        self.PokemonType = PokemonType
        self.PersonalStats = {}
        self.Moves = {}

    def getStat(self, statName):
        # first check if it is a type stat
        typeStat = self.PokemonType.getStat(statName)
        # otherwise check personal stat dictionary
        if typeStat is False or statName in self.PersonalStats:
            return self.PersonalStats[statName]
        else:
            return typeStat

    def addStat(self, statName, statValue):
        # Check if stat already exists
        if statName in self.PersonalStats:
            self.PersonalStats[statName] = statValue
            return True
        else:
            return False

    def printStats(self):
        print("Id: {}".format(self.PokemonType.getId()))
        print("Name: {}".format(self.PokemonType.getName()))
        # print species stats
        for key, value in self.PokemonType.Stats:
            print("{}: {}".format(key,vaue))
        # print individial pokemon stats
        for key, value in self.PersonalStats:
            print("{}: {}".format(key,vaue))
class Pokedex:

    def __init__(self):
        self.PokemonList = {}
        self.TotalPokemon = 0

    def addPokemon(self, Name, Stats):
        tempData = PokemonType(self.TotalPokemon, Name)
        tempData.Stats = dict(Stats)
        self.PokemonList[Name] = tempData
        self.TotalPokemon += 1
    def printPokedex(self):
        for key,value in self.PokemonList.items():
            print ("{}: {}".format(key,value))
    def getPokemon(self, name):
        return self.PokemonList[name]
