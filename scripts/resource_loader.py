# Author: Noah Herrin
# Project: PokemonPY
# Purpose: spreadsheet_manager is a container structure that organizes the process
#          input of a spreadsheet and returns rows as a dictionary, where the key
#          is equal to the column name and the value is the value of the cell. In
#          my project I am using this object to read pokemon config data.
#
import sys
sys.path.insert(0,"D:\Documents\Projects\PyPokemon\storage-files")
import xlrd

# *NOTE* cell(0,0) must contain number of row_names
#        cell(0,1) must contain number of columns
#
# *Process can be made more efficent by storing the spreadsheets within the same file as seperate sheets, would reduce the need to open more workbooks
class spreadsheet_manager:
    def __init__(self,path):
        # initialize spreadsheet and helpful variables
        self.spreadsheet = xlrd.open_workbook("D:\Documents\Projects\PyPokemon\storage-files\{}".format(path))
        self.page = self.spreadsheet.sheet_by_index(0) #*
        self.rows = int(self.page.cell(0,0).value)
        self.columns = int(self.page.cell(0,1).value)
        self.update = True

        # initialize column names prior to fetching rows of real values
        self.row_names = []
        for col in range(self.columns):
            self.row_names.append(self.page.cell(1,col).value.lower())

    # fetches all of the values in a row and returns them as a dictionary
    # of format {'column-name' : 'cell-value'}...
    def fetch_entry(self,row):
        if len(self.row_names) is not 0 and self.update:
            data = {}
            for col in range(self.columns):
                data[self.row_names[col]] = self.page.cell(row,col).value
            return data

    # fetches all entries and returns them as a nested dictionary
    # of format { integer-id : {'column-name':'cell-value',...} }
    def fetch_all_entries(self):
        if len(self.row_names) is not 0 and self.update:
            entries = {}
            id = 0
            for row in range(2,self.rows+2):
                temp = self.fetch_entry(row)
                entries[temp['name']] = temp
                id += 1
                # note to self, techically we don't need to keep storing the value of name in the dictionary but I don't have a reason not to
            return entries

    # toggles boolean switch to prevent accidentally overwriting gamedata
    def toggle_update(self):
        self.update = not update

def load_data(resources):
    data = []
    for key, value in resources.items():
        ssm = spreadsheet_manager(value)
        data.append(ssm.fetch_all_entries())

    return data
