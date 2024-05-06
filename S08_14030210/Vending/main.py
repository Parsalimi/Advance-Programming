from os import system
from vending import Vending
from tool import Tool

     
def Wait():
    input("Press Enter to Continue!!!")

def CleanTerminal():
    system("cls")

# This Function looking for admin in file
def CheckAdmin(username, password):
    file = open("S08_14030210\Vending\\txt_files\\admin.txt","r")
    admins_list = Tool.TxtContentReader(file.read())
    for admin in admins_list:
        if username == admin[0] and password == admin[1]:
            return True
        
    return False

# Admin Login Panel
def LoginPortal():
    CleanTerminal()
    loopContinuing = True
    while loopContinuing:
        CleanTerminal()
        print("ADMIN PANEL")
        username = input("Username: ")
        password = input("Password: ")
        if CheckAdmin(username, password):
            return True
        else:
            pass

# Admin Panel which Admin can do these
# 1. Add Branch - 2. Edit Branch - 3. Delete Branch - 4. Add to Inventory - 5. Delete from Inventory
def AdminPanel():
    if LoginPortal():
        adminPanelFlag = True
        while adminPanelFlag:
            CleanTerminal()
            answer = input("(0 to exit)\n1. Add Branch\n2. Edit Branch\n3. Delete Branch\n4. Add to Inventory\n5. Delete from Inventory\n> ")
            if answer == "0":
                adminPanelFlag = False
                break
            elif answer == "1":
                loopContinuing = True
                while loopContinuing:
                    CleanTerminal()
                    print("Add Branch")
                    print(Vending.ShowBranchesList())
                    branchName = input("What is the Branch name: (0 to exit)\n> ")
                    if branchName == "0":
                        break
                    file = open("S08_14030210\Vending\\txt_files\\branches.txt","a")
                    file.write(f"{branchName},")
                    file.close()
            elif answer == "2":
                loopContinuing = True
                while loopContinuing:
                    CleanTerminal()
                    print("Edit Branch")
                    print(Vending.ShowBranchesList())
                    branchName = input("What is the Branch name: (0 to exit)\n> ")
                    if branchName == "0":
                        break
                    if branchName in Vending.ShowBranchesList():
                        branchNameEdited = input(f"switch {branchName} to ?\n> ")
                        branch_list = []
                        for branch in Vending.ShowBranchesList():
                            if branch == branchName:
                                branch_list.append(branchNameEdited)
                            else:
                                branch_list.append(branch)
                        
                        # Lets create a string to put instead of text of branches
                        branch_text = ""
                        for branch in branch_list:
                            branch_text += f"{branch},"

                        # Lets Place that text
                        file = open("S08_14030210\Vending\\txt_files\\branches.txt","w")
                        file.write(branch_text)
                        file.close()
            elif answer == "3":
                # Delete a Branch
                loopContinuing = True
                while loopContinuing:
                    CleanTerminal()
                    print("Delete Branch")
                    print(Vending.ShowBranchesList())
                    branchName = input("What is the Branch name: (0 to exit)\n> ")
                    if branchName == "0":
                        break
                    if branchName in Vending.ShowBranchesList():
                        branch_list = []
                        for branch in Vending.ShowBranchesList():
                            if branch != branchName:
                                branch_list.append(branch)

                        # Lets create a string to put instead of text of branches
                        branch_text = ""
                        for branch in branch_list:
                            branch_text += f"{branch},"

                        # Lets Place that text
                        file = open("S08_14030210\Vending\\txt_files\\branches.txt","w")
                        file.write(branch_text)
                        file.close()
            elif answer == "4":
                loopContinuing = True
                while loopContinuing:
                    CleanTerminal()
                    print("Add to Inventory Branch")
                    print(Vending.ShowBranchesList())
                    branchName = input("What is the Branch name: (0 to exit)\n> ")
                    if branchName == "0":
                        break
                    if branchName in Vending.ShowBranchesList():
                        addItemFlag = True
                        while addItemFlag:
                            CleanTerminal()
                            print(Vending.ShowBranchInventoryList(branchName))
                            name = input("(0 to exit)\nitem Name: ")
                            if name == "0":
                                addItemFlag = False
                                break
                            count = int(input("Count: "))
                            kind = input("Kind: ")
                            sugarPercent = int(input("Sugar Percent: "))
                            price = float(input("Price: "))
                            detail = input("Detail: ")

                            inventory_text = f"{branchName},{name},{count},{kind},{sugarPercent},{price},{detail}/"

                            file = open("S08_14030210\Vending\\txt_files\\vending_inventory.txt","a")
                            file.write(inventory_text)
                            file.close()

            elif answer == "5":
                loopContinuing = True
                while loopContinuing:
                    CleanTerminal()
                    print("Delete Inventory Branch")
                    print(Vending.ShowBranchesList())
                    branchName = input("What is the Branch name: (0 to exit)\n> ")
                    if branchName == "0":
                        break
                    if branchName in Vending.ShowBranchesList():
                        addItemFlag = True
                        while addItemFlag:
                            CleanTerminal()
                            print(Vending.ShowBranchInventoryList(branchName))
                            name = input("(0 to exit)\nitem Name: ")
                            if name == "0":
                                addItemFlag = False
                                break

                            file = open("S08_14030210\Vending\\txt_files\\vending_inventory.txt","r")
                            branch_inventory_list = Tool.TxtContentReader(file.read())
                            branch_inventory_list.pop(-1)
                            inventory_text = ""
                            for inventory in branch_inventory_list:
                                if inventory[0] != branchName or inventory[1] != name:
                                    inventory_text += f"{inventory[0]},{inventory[1]},{inventory[2]},{inventory[3]},{inventory[4]},{inventory[5]},{inventory[6]}/"
                            file.close()

                            file = open("S08_14030210\Vending\\txt_files\\vending_inventory.txt","w")
                            file.write(inventory_text)
                            file.close()

            
##################
## Main Program ##
##################

flag = True
while flag:
    system("cls")
    answer = input("1. ADMIN PANEL\n2. CUSTOMER\n> ")
    if answer == "1":
        AdminPanel()

    elif answer == "2":
        
        flag = True
        while flag:
            
            CleanTerminal()
            # Show Branches and Select One!
            print("Select Vending Machnie")
            print(Vending.ShowBranchesList())
            branchName = input("What is the Branch name: (0 to exit)\n> ")
            if branchName == "0":
                flag = False
                break
            # if wanted vend selected
            if branchName in Vending.ShowBranchesList():
                selectedVend = Vending(branchName)
                CleanTerminal()
                
                for item in Vending.ShowBranchInventoryList(branchName):
                    print(item[0], end=" | ")

                itemName = input("\nPlease enter the item that you want to buy: ")

                selectedItem = Vending.SelectItemFromInventory(branchName, itemName)
                if selectedItem != False:
                    print(f"Selected Item: {selectedItem.name}")
                    print(f"Price: {selectedItem.price}")
                    print(f"Remaining Count: {selectedItem.count}")
                    answer = input("Do you want to Procced? (yes to continue): ")
                    if answer == "yes":
                        count = int(input(f"How many {selectedItem.name} do you want: "))
                        if count < int(selectedItem.count):
                            print(f"You must pay {count*float(selectedItem.price)}")
                            Vending.BuyDrink(selectedItem, count, branchName)
                            print("Your purchase has been procceded")
                            Wait()
                        else:
                            print("You must enter less item")
                            Wait()