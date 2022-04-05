from ast import Pass
from ctypes import sizeof
import os
import platform
import utils

class VendingMachine:
    def GetItemAndAmount():
        getUserInput = str(input("\nEnter cash amount and item name (e.g. 10 Coke):\n")) 
        if getUserInput == "":
            print("No item/amount was selected/entered")
            return False
        return getUserInput
    
    def SplitCashAmountFromInputString(query):
        counter = 0
        totalAmount = 0
        
        countSpaces = utils.countSpaces(query)
        currCashAmount = query.split(" ",countSpaces)
        currCashAmountLen = len(currCashAmount)

        for coin in currCashAmount:
            if (coin >= '0' and coin <= '9'):
                totalAmount = totalAmount + float(coin)
            else:
                break
            counter = counter + 1
        
        result = currCashAmountLen - counter
        if result != 1:
            print("Invalid coins '"+str(coin)+"' detected!")
            return False
        return totalAmount      

    def SplitItemFromInputString(query):
        countSpaces = utils.countSpaces(query)
        currItem = query.split(" ",countSpaces)
        return currItem[countSpaces]

    def ValidItem(currItemName,l_items):
        try:
            for item in l_items:
                if item['name'].lower() == currItemName.lower():
                    return currItemName
            
            print("Invalid item '"+currItemName+"' selected")
            return False
        except:
            print("Item name is missing")
            return False

    def CalculateChange(currCashAmount,selecteditem,l_items):
        '''
        try:
            currOrigItemPrice = 0
            currCashAmount = query.split(" ",1)
            currFloatAmount = float(currAmount[0])
        except:
            print("Invalid amount entered")
            return
        '''
        for item in l_items:
            if item['name'].lower() == selecteditem.lower():
                currOrigItemName = item['name']
                currOrigItemPrice = float(item['price'])
                if currCashAmount < currOrigItemPrice:
                    print(str(currCashAmount)+" is not enought for "+currOrigItemName)
                else:
                    change = currCashAmount - currOrigItemPrice
                    print(str(change)+" "+currOrigItemName)

    def WelcomeMessage(l_items):
        if platform.system().upper() == "WINDOWS":
            os.system('cls')
        else:
            os.system('clear')
        print("\nVending Machine\n\nWelcome, available items:")
        for i in l_items:
            print(f"{i['name']} - Price: {i['price']}")

    def NextPurchase():
        # exit or continue to another item
        return str(input("\nTo quit the machine enter q and to continue buying enter anything else:")).lower()
