from os import system
import S03_P03_14021214 as cal


def wait():
    input("Press Enter to Continue!!")

class main: 
    Eqution = ""
    equal = 0

def Operation(entrynum):
    while True:
        system('cls')
        print(main.Eqution)
        entryoperation = input("Please Enter your Operation\n(Enter + - / x)\n> ")
        if entryoperation == "+":
            main.Eqution += " +"
            return "+"
        elif entryoperation == "-":
            main.Eqution += " -"
            return "-"
        elif entryoperation == "/":
            main.Eqution += " /"
            return "/"
        elif entryoperation == "x":
            main.Eqution += " x"
            return "x"
        else:
            print("Please Enter an valid answer!")
            wait()

flag = True
th_number = 1
numbers = []


# Main Program
print(main.Eqution)
inputnum = int(input(f"Please enter the {th_number}th number\n> "))
numbers.append(inputnum)
main.Eqution += f" {inputnum}"
th_number += 1
entryoperation = Operation(inputnum)
system("cls")
print(main.Eqution)
inputnum = int(input(f"Please enter the {th_number}th number\n> "))
main.Eqution += f" {inputnum}"
system("cls")
print(main.Eqution)
numbers.append(inputnum)
th_number += 1
main.equal = cal.calulator(numbers[0], numbers[1], entryoperation)
numbers.clear()
answer = input("Do you want to Continue? (no to exit)\n> ")
if answer == "no":
    pass
else:
    while True:
        system("cls")
        print(main.Eqution)
        entryoperation = Operation(inputnum)
        system("cls")
        print(main.Eqution)
        inputnum = int(input(f"Please enter the {th_number}th number\n> "))
        main.Eqution += f" {inputnum}"
        th_number += 1
        system("cls")
        print(main.Eqution)
        main.equal = cal.calulator(main.equal, inputnum, entryoperation)
        numbers.clear()
        answer = input("Do you want to Continue? (no to continue)\n> ")
        if answer == "no":
            break
        
print("answer: ", main.equal)

