'''
Anthony Laymond
1636486
'''
from ReportsController import ReportsController
from datetime import date
import operator
from datetime import datetime


class UI:
    
    def grabResults(self, userInput):#gets the query result based on the user input
        product = []
        lastProduct = []
        dataSplitIntoWords = userInput.split(' ')#splits words into array to be iterated over
        reportsCon = ReportsController()#instance of the reportsController
        totalInven = reportsCon.formFullInventoryList()#gets the full inventory with all columns into a list of lists

        for speci_row in totalInven:#cycle through the inventory
            for word in dataSplitIntoWords:#cycle through the user input words array
                if speci_row[1].strip() == word:#if the word is the same as the manufacturer
                    product.append(speci_row)#then it is a potential match

        for speci_row in product:#cycle over potential options
            for word in dataSplitIntoWords:#cycle over words from input
                if speci_row[2].strip() == word or speci_row[2].strip() == "laptop" and word == "computer" or speci_row[2].strip() == "tower" and word == "computer":#if the given input matches the type of item or if they want to see a computer, then a laptop or tower qualifies as one too
                    lastProduct.append(speci_row)#add it to a potential final output

        if len(lastProduct) >= 1:#if there was a match then return the most expensive item
            return sorted(self.removePastOrDamagedItems(lastProduct), key = operator.itemgetter(3), reverse=True)[0]
        else:#if no match return nothing
            return None

    def removePastOrDamagedItems(self, rawFinalOutput):#removes items that are past service date or are listed as damaged
        filteredLastProduct = []
        for this_row in rawFinalOutput:#loop through the potential final output
            if datetime.strptime(this_row[4], '%m/%d/%Y').date() >= date.today() and this_row[5] != "damaged":#if not damaged and service date is still valid
                filteredLastProduct.append(this_row)#append to true final options
        return filteredLastProduct

    def grabYouMayAlsoConsider(self, selectedItem):#gets the itme to consider based on selected item
        reportsController = ReportsController()
        fullInventory = reportsController.formFullInventoryList()#get full inventory from the reports controller
        possibleItemConsider = None#used to hold value of a found item to consider

        for this_row in fullInventory:#loop through inventory
            if self.removePastOrDamagedItems([this_row]) != []:#dont want damaged or past service items

                if selectedItem[0] != this_row[0] and selectedItem[1] != this_row[1]:#dont want the same item or manufacturer

                    if selectedItem[2] == this_row[2]:#want the same type

                        if possibleItemConsider is None:#if this is the first potential item to consider, then just set the considered item

                            possibleItemConsider = this_row
                        elif abs(int(possibleItemConsider[3]) - int(selectedItem[3])) < abs(int(this_row[3]) - int(selectedItem[3])):#checks which item is closer in value to the queried item
                            possibleItemConsider = this_row

        return possibleItemConsider
                  



    
    