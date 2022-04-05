
import inventory 
import vendingmachine
         
if __name__ == "__main__":
    query = ''
    j_file = "items.json"
    is_quit = False
    currInventoryObj = inventory.Inventory
    currRunObj = vendingmachine.VendingMachine

    while is_quit == False:
        # 1. get inventory items
        items = currInventoryObj.getItems(j_file)
        if not items != False:
            # 1.1 program cannot load items list, exit
            break

        # 2 welcome message and present available items
        currRunObj.WelcomeMessage(items)

        # 3. get user choice and check its valid choice
        query = currRunObj.GetItemAndAmount()
        if query != False:
            # 3.1 get current selected item from query string
            currItem = currRunObj.SplitItemFromInputString(query)
            if currItem != False:            
                # 3.2 get current cash amount from query string
                cashAmount = currRunObj.SplitCashAmountFromInputString(query)
                if cashAmount != False:
                    # 3.3 check selected item is valid
                    itemSelected = currRunObj.ValidItem(currItem,items)
                    if itemSelected != False:
                        # 3.4 check sufficient amount of money was provided
                        currRunObj.CalculateChange(cashAmount,itemSelected.capitalize(),items)
        
        # 4. get user desicion to continue to next purchase
        if currRunObj.NextPurchase() != 'q':
            continue
        is_quit = True
       

