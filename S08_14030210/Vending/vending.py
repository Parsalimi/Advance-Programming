from tool import Tool
from inventory import VendingItem

class Vending:

    def __init__(self,name):
        self.name = name

    def ShowBranchesList():
        file = open("Vending\\txt_files\\branches.txt","r")
        branches_text = file.read()
        file.close()
        branches_list = branches_text.split(",")
        branches_list.pop(-1)
        return branches_list
    
    def ShowBranchInventoryList(branchName):
        file = open("Vending\\txt_files\\vending_inventory.txt","r")
        branch_inventory_list = Tool.TxtContentReader(file.read())
        final_list = []
        for inventory in branch_inventory_list:
            if inventory[0] == branchName:
                final_list.append([inventory[1],inventory[2],inventory[3],inventory[4],inventory[5],inventory[6]])
        file.close()

        return final_list
    
    def SelectItemFromInventory(branchName, itemName):
        for item in Vending.ShowBranchInventoryList(branchName):
            if item[0] == itemName:
                selectedItem = VendingItem(item[0],item[1],item[2],item[3],item[4],item[5])
                return selectedItem
        return False

    
    
    def BuyDrink(selectedItem, count, branchName):
        count = int(selectedItem.count) - count

        # Update the Database ;)
        file = open("Vending\\txt_files\\vending_inventory.txt","r")
        branch_inventory_list = Tool.TxtContentReader(file.read())
        branch_inventory_list.pop(-1)
        inventory_text = ""
        for inventory in branch_inventory_list:
            if inventory[0] == branchName and inventory[1] == selectedItem.name:
                inventory_text += f"{branchName},{selectedItem.name},{count},{selectedItem.kind},{selectedItem.percentOfSugar},{selectedItem.price},{selectedItem.detail}/"
            else:
                inventory_text += f"{inventory[0]},{inventory[1]},{inventory[2]},{inventory[3]},{inventory[4]},{inventory[5]},{inventory[6]}/"

        file.close()

        file = open("Vending\\txt_files\\vending_inventory.txt","w")
        file.write(inventory_text)
        file.close()