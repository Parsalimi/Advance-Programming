# Gereftan esm
# generate id
# search id option
# save on txt

from random import randint
from os import system

users = []
column = '| '
######################
# The users.txt indexing GUIDE:
# 0  |     1    |     2    |    3   |    4   |   5   |  6  |   7
# ID | username | password | f_name | l_name | email | age | uni_id
######################
def wait():
    input("To Continue Press Enter!!!")

def UpdateUsersList():
    users.clear()
    lastIndexLine = 2
    file = open("S07_14030203\\user_db\\users.txt","r")
    for userLine in file:
        selected_user = userLine.split(",")
        selected_user[lastIndexLine] = selected_user[lastIndexLine].strip()
        users.append({"ID": selected_user[0], 
                      "Username": selected_user[1], 
                      "Password": selected_user[2], 
                      "First Name": selected_user[3],
                      "Last Name": selected_user[4],
                      "Email": selected_user[5],
                      "Age": selected_user[6],
                      "uni_id": selected_user[7]})
    file.close()
        
def add_user():
    UpdateUsersList()
    system('cls')
    username = input("username: ")
    password = input("password: ")
    f_name = input("First Name: ")
    l_name = input("Last Name: ")
    email = input("Email: ")
    age = input("age: ")
    uni_id = randint(10000000,99999999)

    # Looking for Last ID
    file = open("S07_14030203\\user_db\\last_user_login_id.txt", "r")
    last_user_login_id = file.read()
    file.close()

    last_user_login_id = int(last_user_login_id)+1

    file = open("S07_14030203\\user_db\\users.txt", "a")
    file.write(f"\n{last_user_login_id},{username},{password},{f_name},{l_name},{email},{age},{uni_id}")
    file.close()

    
    file = open("S07_14030203\\user_db\\last_user_login_id.txt", "w")
    file.write(str(last_user_login_id))
    file.close()

    

def ShowUsers():
    UpdateUsersList()
    system('cls')
    for acc in users:
        print(f"{acc["ID"]:<1} | {acc["Username"]:<10} | {acc["Password"]:<10} | {acc["First Name"]:<10} | {acc["Last Name"]:<20} | {acc["Email"]:<25} | {acc["Age"]:<3} | {acc["uni_id"]:<9}",end="")
    print()
    wait()

def SearchUser():
    UpdateUsersList()
    while True:
        system('cls')
        print("0 to exit")
        answer = input("Please enter the user ID\n> ")
        if answer == "0":
            break
        else:
            for acc in users:
                uni_id = acc["uni_id"]
                uni_id = uni_id.strip("\n")
                if uni_id == answer:
                    print(f"{acc["ID"]:<2} | {acc["Username"]} | {acc["Password"]} | {acc["First Name"]} | {acc["Last Name"]} | {acc["Email"]} | {acc["Age"]} | {acc["uni_id"]}",end="")
        print()
        wait()

#TODO: FIX THIS
def DeleteUser():
    while True:
        system('cls')
        print("0 to exit")
        answer = input("Please enter the user ID\n> ")
        textToWriteInFile = ""
        for acc in users:
            if acc["ID"] == answer:
                pass
            else:
                textToWriteInFile = f"{acc["ID"]},{acc["Username"]},{acc["Password"]},{acc["First Name"]},{acc["Last Name"]},{acc["Email"]},{acc["Age"]},{acc["uni_id"]}\n"

        file = open("S07_14030203\\user_db\\users.txt","w")
        file.write(textToWriteInFile)
        file.close()
        UpdateUsersList()
                
        
flag = True
while flag:
    UpdateUsersList()
    system('cls')
    print("0 to exit!")
    answer = input("1. Show Users\n2. Add User\n3. Search User\n4. Delete User\n> ")
    if answer == "1":
        ShowUsers()
    elif answer == "2":
        while True:
            add_user()
            answer = input("Do you want to add anonther user?")
            if answer == "no":
                break
    elif answer == "3":
        SearchUser()
    elif answer == "4":
        DeleteUser()
    elif answer == "0":
        flag = False
    else:
        print("Give me an Valid answer!")
        wait()