from managment import Managment
from tools import *

####################
### MAIN PROGRAM ###
####################

flag = True
while flag:
    ClearTerminal()
    answer = input("1. Add Student\n2. Show Students\n3. Search Student\n4. Remove Student\n5. Edit Student\n> ")
    if answer == "1":
        Managment.AddStudent()
    elif answer == "2":
        Managment.ShowStudents()
        Wait()
    elif answer == "3":
        Managment.SearchStudent()
        Wait()
    elif answer == "4":
        Managment.DeleteStudent()
    elif answer == "5":
        Managment.EditStudent()
    else:
        ClearTerminal()
        print(ColoredNotification("Wrong Input, Please Try Again","red"))
        Wait()