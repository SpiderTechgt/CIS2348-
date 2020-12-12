'''
Anthony Laymond
1636486
'''
import csv
import operator

class ItemTypeListController:

    def __init__(self, file_path):
        self.file_path = file_path

    def graballProductTypes(self):
        reader = csv.reader(open(self.file_path), delimiter=",")
        sorted_manufacturer_names = sorted(reader, key=operator.itemgetter(2))
        return self.grabsplitTypeData(sorted_manufacturer_names)
    
    def grabsplitTypeData(self, inputList):#creates a dictionary with the key being the type and the value being an array with a type in that category
        typesDictionary = {}
        for this_type in inputList:#inputList will be the full inventory
            if this_type[2] not in typesDictionary:#if doesnt exist in the dictionary
                typesDictionary[this_type[2]] = [this_type]#create a new listing and initialize it
            else:

                typesDictionary[this_type[2]].append(this_type)#append it to already created category in dictionary

        return typesDictionary

            
