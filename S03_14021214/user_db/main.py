from os import system

users = []
column = '\t | '
######################
# The users.txt indexing GUIDE:
# 0  |     1    |     2    |    3   |    4   |   5   |  6
# ID | username | password | f_name | l_name | email | age
######################
def wait():
    input("To Continue Press Enter!!!")

def UpdateUsersList():
    users.clear()
    lastIndexLine = 2
    file = open("users.txt","r")
    for userLine in file:
        selected_user = userLine.split(",")
        selected_user[lastIndexLine] = selected_user[lastIndexLine].strip()
        users.append({"ID": selected_user[0], 
                      "Username": selected_user[1], 
                      "Password": selected_user[2], 
                      "First Name": selected_user[3],
                      "Last Name": selected_user[4],
                      "Email": selected_user[5],
                      "Age": selected_user[6]})
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

    # Looking for Last ID
    file = open("last_user_login_id.txt", "r")
    last_user_login_id = file.read()
    file.close()

    last_user_login_id = int(last_user_login_id)+1

    file = open("users.txt", "a")
    file.write(f"\n{last_user_login_id},{username},{password},{f_name},{l_name},{email},{age}")
    file.close()

    
    file = open("last_user_login_id.txt", "w")
    file.write(str(last_user_login_id))
    file.close()

    

def ShowUsers():
    UpdateUsersList()
    system('cls')
    for acc in users:
        print(acc["ID"], column,
              acc["Username"], column, 
              acc["Password"], column,
              acc["First Name"], column,
              acc["Last Name"], column,
              acc["Email"], column,
              acc["Age"],
              end="")
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
                if acc["ID"] == answer:
                    print(  acc["ID"], column,
                            acc["Username"], column, 
                            acc["Password"], column,
                            acc["First Name"], column,
                            acc["Last Name"], column,
                            acc["Email"], column,
                            acc["Age"],
                            end="")
        print()
        wait()

def DeleteUser():
    while True:
        system('cls')
        print("0 to exit")
        answer = input("Please enter the user ID\n> ")
        file = open("test.txt","a")
        for acc in users:
            if acc["ID"] == answer:
                pass
            else:
                file.write(f"{acc[0]},{acc[1]},{acc[2]},{acc[3]},{acc[4]}")
                
        
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