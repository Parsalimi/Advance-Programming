# solid_entry = input("Enter the Eqution: ")
# solid_entry = solid_entry.split(" ")
solid_entry = [['('], [3], ['+'], [2], [')'], ['x'], [7]]

def Solve(Equtions):
    index = 0
    # Second Priority
    while index < len(Equtions):
        if Equtions[index][0] == "x":
            answer = Equtions[index-1][0] * Equtions[index+1][0]
            Equtions[index][0] = answer
            Equtions.pop(index-1)
            Equtions.pop(index)
            index -= 1
        if Equtions[index][0] == "/":
            if Equtions[index-1][0] == 0 or Equtions[index+1][0] == 0:
                print("You can't divide anything by zero\nOr zero by anything")
                break
            answer = Equtions[index-1][0] / Equtions[index+1][0]
            Equtions[index][0] = answer
            Equtions.pop(index-1)
            Equtions.pop(index)
            index -= 1
        index += 1

    index = 0
    # Third Priority
    while index < len(Equtions):
        if Equtions[index][0] == "+":
            answer = Equtions[index-1][0] + Equtions[index+1][0]
            Equtions[index][0] = answer
            Equtions.pop(index-1)
            Equtions.pop(index)
            index -= 1
        if Equtions[index][0] == "-":
            answer = Equtions[index-1][0] - Equtions[index+1][0]
            Equtions[index][0] = answer
            Equtions.pop(index-1)
            Equtions.pop(index)
            index -= 1
        index += 1

    return Equtions

def Parantezis_finder(Equtions):
    for index, item in enumerate(Equtions):
        if item[0] == ')':
            for i in range(index, -1, -1):
                if Equtions[i][0] == '(':
                    result = Solve(Equtions[i+1: index])[0][0]
                    lenght = index - i + 1
                    for j in range(0, lenght-1):
                        Equtions.pop(i)
                    Equtions[i] = [result]
                    return Equtions
                
print(Solve(Parantezis_finder(solid_entry))[0][0])