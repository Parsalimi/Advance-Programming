from tools import *
from managment import Managment

flag = True
while flag:
    ClearTerminal()
    answer = input("1. Show Book\n2. Add Book\n3. Delete Book\n4. Edit Book\n5. Search Book\n> ")
    if answer == "1":
        Managment.ShowBooks()
        Wait()
    elif answer == "2":
        Managment.AddBook()
        Wait()
    elif answer == "3":
        Managment.DeleteBook()
        Wait()
    elif answer == "4":
        Managment.EditBook()
        Wait()
    elif answer == "5":
        Managment.SearchBook()
        Wait()
    else:
        ClearTerminal()
        print(ColoredNotification("Invalid input. Please try again.","red"))
        Wait()