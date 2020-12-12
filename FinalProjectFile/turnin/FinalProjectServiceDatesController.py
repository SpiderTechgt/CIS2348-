'''
Anthony Laymond
1636486
'''
import csv

class ServiceDatesListController:

    def __init__(self, file_path):
        self.file_path = file_path
    
    def grabManufacturerforServiceDateOfAllProducts(self, manufacturer_data):#add service date to previous addition of price to manufacturer List and Price list CSV combination
        reader = csv.reader(open(self.file_path), delimiter=",")#read file
        manufacturer_data_with_date = []
        for line in reader:#for line in ServiceDatesList CSV reader
            for manufacturer_line in manufacturer_data:#for row in inventory list with price data
                if line[0] == manufacturer_line[0]:#if id matches
                    manufacturer_line.insert(4,line[1])#add service date column to this row
                    manufacturer_data_with_date.append(manufacturer_line)#add listing to new output list
                    break
        return manufacturer_data_with_date