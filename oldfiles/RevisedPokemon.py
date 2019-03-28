class Pokemon:
    def __init__(self,name):
        self.Name = name
        self.Data = {
            "Name" : name
        }
class PokemonManager:
    def __init__(self):
        self.MasterList = {}
    def addMasterCopy(self, name, data):
        
