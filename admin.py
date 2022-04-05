import inventory 

if __name__ == "__main__":
    j_file = "items.json"
    currInventoryObj = inventory.Inventory
    
    while True:
        # 1. print welcome message and get user input
        currUserSelection = currInventoryObj.WelcomeMessage()
        
        # 2. route user selection
        if currUserSelection == "a":
            # 2.1 add item to inventory
            currInventoryObj.addItem(j_file)
        elif currUserSelection == "d":
            # 2.2  delete item from inventory
            currInventoryObj.deleteItem(j_file)
        elif currUserSelection == "q":
            # quit operations panel
            break
        else:
            print("Wrong input!")

        # 3. get user desicion to continue to next purchase
        if currInventoryObj.NextAction() == 'q':
            break
    
        
    