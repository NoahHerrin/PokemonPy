from GameLoader import Loader
from Pokemon import PokemonType
from Pokemon import Pokemon
from Pokemon import Pokedex
import os
pd = Pokedex()
names = ["Charmander", "Charmeleon","Charizard"]
stats = {
    "type" : "fire",
    "catch-rate": "39"
}
for i in range(len(names)):
    pd.addPokemon(names[i],stats)
    pd.getPokemon(names[i]).printDetails()
#loader = Loader()
#pd = loader.loadPokemonData("pokemondata.txt")
#pd.printPokedex()
