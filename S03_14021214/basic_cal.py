from os import system

def wait():
    input("Press Enter to Continue!!")

def Header():
    system("cls")
    print(main.Eqution)

class main: 
    Eqution = ""
    Equtions = []

def Operation():
    while True:
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
        elif entryoperation == "n":
            return "n"
        else:
            print("Please Enter an valid answer!")
            wait()

flag = True
th_number = 1
main_Program = True

# Main Program
Header()
# Get Number
inputnum = int(input(f"Please enter the {th_number}th number\n> "))
main.Eqution += f"{inputnum}"
th_number += 1
main.Equtions.append([inputnum])

Header()
# Operation
entryoperation = Operation()
main.Equtions.append([entryoperation])

while main_Program:
    Header()

    # Get Number
    inputnum = int(input(f"Please enter the {th_number}th number\n> "))
    main.Eqution += f" {inputnum}"
    th_number += 1
    main.Equtions.append([inputnum])

    Header()
    if th_number > 2:
        print("To quit enter 'n'")
    # Operation
    entryoperation = Operation()
    if entryoperation == 'n':
        main_Program = False
        break
    main.Equtions.append([entryoperation])
        
index = 0
# Second Priority
while index < len(main.Equtions):
    if main.Equtions[index][0] == "x":
        answer = main.Equtions[index-1][0] * main.Equtions[index+1][0]
        main.Equtions[index][0] = answer
        main.Equtions.pop(index-1)
        main.Equtions.pop(index)
        index -= 1
    if main.Equtions[index][0] == "/":
        answer = main.Equtions[index-1][0] / main.Equtions[index+1][0]
        main.Equtions[index][0] = answer
        main.Equtions.pop(index-1)
        main.Equtions.pop(index)
        index -= 1
    index += 1

index = 0
# Third Priority
while index < len(main.Equtions):
    if main.Equtions[index][0] == "+":
        answer = main.Equtions[index-1][0] + main.Equtions[index+1][0]
        main.Equtions[index][0] = answer
        main.Equtions.pop(index-1)
        main.Equtions.pop(index)
        index -= 1
    if main.Equtions[index][0] == "-":
        answer = main.Equtions[index-1][0] - main.Equtions[index+1][0]
        main.Equtions[index][0] = answer
        main.Equtions.pop(index-1)
        main.Equtions.pop(index)
        index -= 1
    index += 1

Header()
print("Answer: ", main.Equtions[0][0])

