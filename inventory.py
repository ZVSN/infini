import json
import os
import platform

class Inventory:
    def getItems(currFile):
        data = Inventory.openFile(currFile,'r')
        if data != False:
            items = json.load(data)
            Inventory.closeFile(data)
            return items
        return False

    def validateAddNameInput():
        try:
            currName = str(input("\nEnter name of item to add:"))
            if currName.replace(" ","").isalpha() == False:
                print("Selected item name have to contains only letters!")
                return False
            return currName
        except ValueError:
            print("Selected item name is not string!")
            return False

    def validateAddPriceInput(currName):
        try:
            currPrice = float(input("Enter price of "+str(currName)+":"))
            return currPrice
        except ValueError:
            print("Selected price is not float/integer")
            return False

    def addItem(currFile):
        getAddItemName = Inventory.validateAddNameInput()
        if getAddItemName == False:
            return False
        getAddItemPrice = Inventory.validateAddPriceInput(getAddItemName)
        if getAddItemPrice == False:
            print("\nProgram cannot add new item!")
            return False
        # append item to current list
        updatedItems = Inventory.getItems(currFile)
        updatedItems.append({'name': getAddItemName, 'price': getAddItemPrice})
        # write updated list to json file
        data = Inventory.openFile(currFile,'w')
        json.dump(updatedItems,data)
        Inventory.closeFile(data)
        print("\nNew item added '"+getAddItemName+"', Price is '"+str(getAddItemPrice)+"'\n")

    def deleteItem(currFile):
        itemsCounter = 0
        getDelItemName = str(input("\nEnter name of item to delete:"))
        updatedItems = Inventory.getItems(currFile)
        for i in range(len(updatedItems)):
            if getDelItemName.lower() in updatedItems[i].get('name').lower():
                print(updatedItems[i], end="\n")
                break
            itemsCounter += 1
        if itemsCounter != len(updatedItems):
            del updatedItems[itemsCounter]
            data = Inventory.openFile(currFile,'w')
            json.dump(updatedItems,data)
            Inventory.closeFile(data)
            print("\nThe item '"+getDelItemName+"' is deleted!\n")
        else:
            print("\nThe item '"+getDelItemName+"' not found in inventory items!\n")

    def openFile(currOpenFile,currMode):
        try:
            f = open(currOpenFile,mode=currMode)
            return f
        except (FileNotFoundError, IOError):
            print("\nFile '"+currOpenFile+"' not found\n")
            return False

    def closeFile(currCloseFile):
        try:
            currCloseFile.close()
        except (FileNotFoundError, IOError):
            print("\nCannot close '"+currCloseFile+"' file\n")
            return False

    def WelcomeMessage():
        menuConStr = "[a] Add item to inventory\n[d] Delete item from inventory\n[q] Quit\n\nSelection:\n"
        if platform.system().upper() == "WINDOWS":
            os.system('cls')
        else:
            os.system('clear')
        print("\nVending Machine\n\nOperations Panel:")
        return str(input(menuConStr)).lower()

    def NextAction():
        # exit or continue to another action
        return str(input("\nTo quit the operations panel enter q and to continue next action enter anything else:")).lower()


