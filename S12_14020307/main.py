from tools import *
from book_managment import BookManagment as bm
from admin_managment import AdminManagment as am

def UserPanel():
    userPanelLoop = True
    while userPanelLoop:
        ClearTerminal()
        answer = input("1. Show Book\n2. Search Book\n(0 to exit)\n> ")
        if answer == "1":
            bm.ShowBooks()
            Wait()
        elif answer == "2":
            bm.SearchBook()
            Wait()
        elif answer == "0":
            break
        else:
            ClearTerminal()
            print(ColoredNotification("Invalid input. Please try again.","red"))
            Wait()

def AdminLogin():
    adminLoginLoop = True
    while adminLoginLoop:
        ClearTerminal()
        print("(0 to exit)")
        username = input("Username: ")
        if username == "0":
            break
        password = input("Password: ")
        if am.Login(username,password):
            ClearTerminal()
            print(ColoredNotification("Welcome!!!","green"))
            Wait()
            AdminPanel()
        else:
            ClearTerminal()
            print(ColoredNotification("Invalid username or password. Please try again.","red"))
            Wait()
    
def AdminPanel():
    adminPanelLoop = True
    while adminPanelLoop:
        ClearTerminal()
        answer = input("1. Show Book\n2. Add Book\n3. Delete Book\n4. Edit Book\n5. Search Book\n(0 to exit)\n> ")
        if answer == "1":
            bm.ShowBooks()
            Wait()
        elif answer == "2":
            bm.AddBook()
            Wait()
        elif answer == "3":
            bm.DeleteBook()
            Wait()
        elif answer == "4":
            bm.EditBook()
            Wait()
        elif answer == "5":
            bm.SearchBook()
            Wait()
        elif answer == "0":
            break
        else:
            ClearTerminal()
            print(ColoredNotification("Invalid input. Please try again.","red"))
            Wait()

flag = True
while flag:
    ClearTerminal()
    answer = input("1. User Panel\n2. Admin Panel\n> ")
    if answer == "1":
        UserPanel()
    elif answer == "2":
        AdminLogin()
    else:
        ClearTerminal()
        print(ColoredNotification("Invalid input. Please try again.","red"))
        Wait()