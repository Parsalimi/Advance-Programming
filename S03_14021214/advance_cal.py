from os import system
class main:
    Eqution = []

# This function will convert the entry to the our format to do all computations
def ConvertEntry(equtionStr: str):
    looking_list = ['(',')','+','-','x','/']
    last_important_index = 0

    equtionStr = equtionStr.replace(" ", "")

    for index, char in enumerate(equtionStr):
        if char in looking_list:
            if index > 0:
                if len(main.Eqution) == 0:
                    main.Eqution.append(equtionStr[0:index])
                    main.Eqution.append(char)
                    last_important_index = index
                else:
                    main.Eqution.append(equtionStr[last_important_index+1:index])
                    main.Eqution.append(char)
                    last_important_index = index
            else:
                main.Eqution.append(char)

    main.Eqution.append(equtionStr[last_important_index+1:len(equtionStr)]) # append the remain number 

    # remove gaps
    for item in main.Eqution:
        if item == '':
            main.Eqution.remove(item)

    # convert needed strings to int
    for index, item in enumerate(main.Eqution):
        if item not in looking_list:
            main.Eqution[index] = float(item)

# This Function will Check How many Parentheses used in it and if there is a problem it will report it
def ParenthesesChecker():
    openParenthesesCount = 0
    closeParenthesesCount = 0

    for item in main.Eqution:
        if item == '(':
            openParenthesesCount += 1
        elif item == ')':
            closeParenthesesCount += 1
            
    if openParenthesesCount != closeParenthesesCount:
        print("The Eqution is not RIGHT!!!")
        quit()
    else:
        return openParenthesesCount # Return Count of Parentheses

def Solve(Equtions):
    index = 0
    # Second Priority
    while index < len(Equtions):
        if Equtions[index] == "x":
            answer = Equtions[index-1] * Equtions[index+1]
            Equtions[index] = answer
            Equtions.pop(index-1)
            Equtions.pop(index)
            index -= 1
        if Equtions[index] == "/":
            if Equtions[index-1] == 0 or Equtions[index+1] == 0:
                print("You can't divide anything by zero\nOr zero by anything")
                break
            answer = Equtions[index-1] / Equtions[index+1]
            Equtions[index] = answer
            Equtions.pop(index-1)
            Equtions.pop(index)
            index -= 1
        index += 1

    index = 0
    # Third Priority
    while index < len(Equtions):
        if Equtions[index] == "+":
            answer = Equtions[index-1] + Equtions[index+1]
            Equtions[index] = answer
            Equtions.pop(index-1)
            Equtions.pop(index)
            index -= 1
        if Equtions[index] == "-":
            answer = Equtions[index-1] - Equtions[index+1]
            Equtions[index] = answer
            Equtions.pop(index-1)
            Equtions.pop(index)
            index -= 1
        index += 1

    return Equtions[0]

def ParenthesesSolver():
    for index, item in enumerate(main.Eqution):
        if item == ')':
            for i in range(index, -1, -1):
                if main.Eqution[i] == '(':
                    result = Solve(main.Eqution[i+1: index])
                    lenght = index - i + 1
                    for j in range(0, lenght-1):
                        main.Eqution.pop(i)
                    main.Eqution[i] = result
                    return main.Eqution

# THE MAIN PROGRAM STARTS HERE
system('cls')
eqution_str = input("Please Enter your MATH Problem\n> ")   
ConvertEntry(eqution_str)
for z in range(0, ParenthesesChecker()):
    ParenthesesSolver()
Solve(main.Eqution)
print(main.Eqution[0])

import time