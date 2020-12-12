'''
Anthony Laymond
1636486
'''
import csv
import operator

from ServiceDatesController import *
from ItemTypeListController import *
from PriceListController import *
from ManufacturerListController import *

from datetime import datetime
from datetime import date

class ReportsController:

    
    def formFullInventoryList(self):
        serviceDatesController = ServiceDatesListController('CSV/ServiceDatesList.csv')#create objects of each Controller

        priceController = PriceListController('CSV/PriceList.csv')

        manufacturerController = ManufacturerListController('CSV/ManufacturerList.csv')

        manuList = manufacturerController.grabSortofManufacturerAllProducts()#call this to make initial list of manufacturer data i nManufacturerList CSV

        priceList = priceController.grabManufacturerforPriceOfAllProduct(manuList)#call this to add price data to the above list

        lastProduct = serviceDatesController.grabManufacturerforServiceDateOfAllProducts(priceList)#call this to add service date data to the above list

        return sorted(lastProduct, key = operator.itemgetter(1)) #sort by manufacturer name


    def formFullInventoryCSV(self):#write full inventory list to CSV
        self.writeToFile("CSV/FullInventory.csv", self.formFullInventoryList())

    def formItemInventoryDictionary(self):#creates the item inventory dictionary to then create the different typeInventory CSV files
        itemTypeListController = ItemTypeListController('CSV/ManufacturerList.csv')#create instances of each controller needed
        priceController = PriceListController('CSV/PriceList.csv')
        serviceDatesController = ServiceDatesListController('CSV/ServiceDatesList.csv')

        itemTypesDictionary = itemTypeListController.graballProductTypes()#gets dictionary of all the data separated with only manufacturer List CSV data
        
        for speci_type in itemTypesDictionary.keys():
            itemTypesDictionary[speci_type] = priceController.grabManufacturerforPriceOfAllProduct(itemTypesDictionary[speci_type])#add price data to each row
            itemTypesDictionary[speci_type] = serviceDatesController.grabManufacturerforServiceDateOfAllProducts(itemTypesDictionary[speci_type])#add service date data to each row
        
        return itemTypesDictionary

    def writeToFile(self, fileName, tableData):#general function for writing to file for given list data
        with open(fileName, 'w', newline="") as new_file:
            csv_writer = csv.writer(new_file, delimiter=",")

            for line in tableData:
                csv_writer.writerow(line)
    
    def writeAllTypeInventoryListstoCSV(self):#writes the different typeInventory files to CSV

        finalData = self.formItemInventoryDictionary()#get the complete separated dictionary with the categories matching to their list of rows

        for each_type in finalData.keys(): #for each key in dictionary, write the list associated to them to a file

            self.writeToFile("CSV/"+each_type+"Inventory.csv", finalData[each_type])
    
    def formPastServicesList(self):#create the list with all the services of the past
        fullTable = self.formFullInventoryList()#get the full inventoyr
        lastProduct = []
        for each_row in fullTable:#iterate over each row
            listingDate = datetime.strptime(each_row[4], '%m/%d/%Y').date()
            if listingDate < date.today():#if its from a date in the past
                lastProduct.append(each_row)#add it to output array
        return sorted(lastProduct, key=lambda x: datetime.strptime(x[4], '%m/%d/%Y'), reverse=True) #return array sorted by most recent
    
    def formPastServicesCSV(self):#used to write the past services data to the file
        self.writeToFile("CSV/PastServicesDateInventory.csv", self.formPastServicesList())

    def formDamagedInventoryList(self):#create damaged inventory list
        compleTable = self.formFullInventoryList()#get full inventory
        lastProduct = []

        for speci_row in compleTable:#iterate over each row in inventory
            if speci_row[5] == "damaged":#if it is damaged
                lastProduct.append(speci_row)#append ot output array
        return sorted(lastProduct, key = operator.itemgetter(3), reverse=True)#return sorted by most expensive to least expensive
    
    def formDamagedInventoryCSV(self):#write the damaged inventory list to a file
        self.writeToFile("CSV/DamagedInventory.csv", self.formDamagedInventoryList())
