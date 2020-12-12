'''
Anthony Laymond
1636486
'''
import csv

class PriceListController:

    def __init__(self, file_path):

        self.file_path = file_path
    
    def grabManufacturerforPriceOfAllProduct(self, manufacturer_data):#from manufacturer data list, add price data to corresponding IDs

        reader = csv.reader(open(self.file_path), delimiter=",")#read file
        manufacturer_data_price = []

        for line in reader:#for each row in Price List CSV

            for manufacturer_line in manufacturer_data:#for each row in manufacturer list

                if line[0] == manufacturer_line[0]:# if the id matches

                    manufacturer_line.insert(3,line[1])#add price column to row

                    manufacturer_data_price.append(manufacturer_line)#add this array to new output array

                    break#break to prevent extra searching

        return manufacturer_data_price
    

    