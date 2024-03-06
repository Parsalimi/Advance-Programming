from os import system
import Calculator as cal


def wait():
    input("Press Enter to Continue!!")

class main: 
    Eqution = ""
    equal = 0
    Equtions = []

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

# Getting First Number
inputnum = int(input(f"Please enter the {th_number}th number\n> "))
numbers.append(inputnum)
main.Eqution += f"{inputnum}"
th_number += 1
main.Equtions.append([inputnum,"",0])
# Operation
entryoperation = Operation(inputnum)
main.Equtions[th_number-2][1] = entryoperation
system("cls")
print(main.Eqution)
inputnum = int(input(f"Please enter the {th_number}th number\n> "))
main.Eqution += f" {inputnum}"
main.Equtions[th_number-2][2] = inputnum
system("cls")
print(main.Eqution)
numbers.append(inputnum)
th_number += 1 # 3
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
        main.Equtions.append([inputnum,entryoperation,0])
        system("cls")
        print(main.Eqution)
        inputnum = int(input(f"Please enter the {th_number}th number\n> "))
        main.Eqution += f" {inputnum}"
        main.Equtions[th_number-2][2] = inputnum
        th_number += 1
        system("cls")
        print(main.Eqution)
        main.equal = cal.calulator(main.equal, inputnum, entryoperation)
        numbers.clear()
        answer = input("Do you want to Continue? (no to exit)\n> ")
        if answer == "no":
            break
        
print(main.Equtions)
for sub_eq in main.Equtions:
    if sub_eq[1] == "x":
        answer = sub_eq[0] * sub_eq[2]
    elif sub_eq[1] == "/":
        answer = sub_eq[0] / sub_eq[2]
print("answer: ", main.equal)

