from tools import *
from account import Account

def AddBankAccount():
    ClearTerminal()
    cardOwnerName = input("Enter Your the Card Owner Name: ")
    cardNumber = input("Enter Your Card Number: ")
    balance = float(input("Enter your Balance: "))
    selectedAccount = Account(cardOwnerName, cardNumber, balance)
    with open("S10_14020224\\bank\\db\\customers.txt", "a") as file:
        file.write(f"{selectedAccount.name},{selectedAccount.cardNumber},{selectedAccount.balance}\n")
        file.close

def ShowBankAccounts():
    ClearTerminal()
    with open("S10_14020224\\bank\\db\\customers.txt", "r") as file:
        print(file.read())
    Wait()

#####################
#### Main Program ###
#####################

flag = True
while flag:
    ClearTerminal()
    answer = input("1. Add Bank Account\n2. Show Bank Accounts\n> ")
    if answer == "1":
        AddBankAccount()
    elif answer == "2":
        ShowBankAccounts()
    else:
        print("Wrong Input!!!")
        Wait()