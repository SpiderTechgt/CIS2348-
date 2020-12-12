'''
Anthony Laymond
163486
'''

import csv
import operator

class ManufacturerListController:

    def __init__(self, file_path):
        self.file_path = file_path

    def grabSortofManufacturerAllProducts(self):#creates list of everything from ManufacturerList CSV

        opener = csv.reader(open(self.file_path), delimiter=",")#read file for manufacturer list csv

        sorted_manu_names = sorted(opener, key=operator.itemgetter(1))#sorts the list of lists based on the manufacturer name (column 1)

        manu_names = []

        for each_name in sorted_manu_names:#for each one, append it to final array

            manu_names.append(each_name)

        return manu_names
