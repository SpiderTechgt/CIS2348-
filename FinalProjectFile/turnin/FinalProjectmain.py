'''Anthony Laymond
1636486
'''
import csv
import operator
from ItemTypeListController import ItemTypeListController
from UI import UI
from ReportsController import ReportsController



reportsController = ReportsController() # create instance of the Reports Controller
print("Creating Full Inventory CSV...")
reportsController.formFullInventoryCSV() #this function calls other functions within in it to create the FullInventory CSV file

print("Creating Different Types Inventory CSV...")
reportsController.writeAllTypeInventoryListstoCSV()#this function calls other functions within in it to create the various type CSV file

print("Creating Past Services CSV...")
reportsController.formPastServicesCSV()#this function calls other functions within in it to create the Past Services CSV file

print("Creating Damaged Inventory CSV...")
reportsController.formDamagedInventoryCSV()#this function calls other functions within in it to create the Damaged Inventory CSV file


ui = UI()#this creates an instance of the UI class so that we can use its functions
while True:#is an infinite loop until the user types q
    userInput = input("\nSearch for an item by Manufacturer and Type: ")#get user input

    if userInput == 'q':#if user enters q then then the loop is broken and the program ends

        break


    product = ui.grabResults(userInput)#this function gets the result from the inventory based on the user input
    if product is not None:#this is to check if no item was found

        optionToConsider = ui.grabYouMayAlsoConsider(product)# if an item was found then this searches for a similar item
        print("Your item is: " + product[0] + ", " + product[1] + ", " + product[2] + ", " + product[3] + "\n")

        if optionToConsider != None:
            print("You may also want to consider the options: " + optionToConsider[0] + ", " + optionToConsider[1] + ", " + optionToConsider[2] + ", " + optionToConsider[3] + "\n")
        else:
            print("No other options alike to consider.\n")
    else:
        print("No such item in inventory\n")
        print("No other options alike to consider.\n")
    print("click q then click enter to quit")
