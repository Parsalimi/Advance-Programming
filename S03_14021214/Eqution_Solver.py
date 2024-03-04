from os import system

parantez_open = []
parantez_close = []

def ParantezOpenCheck(txt):
    if txt == "(":
        return True

def ParantezCloseCheck(txt):
    if txt == ")":
        return True
    
    

def Parantez(txt):
    for i in range(0, len(txt)):
        if ParantezOpenCheck(txt[i]) == True:
            parantez_open.append(i)

    for i in range(0, len(txt)):
        if ParantezCloseCheck(txt[i]) == True:
            parantez_close.append(i)

system('cls')
Eqution = input("Please Enter the Eqution: ")
Parantez(Eqution)
print(parantez_open, parantez_close)
parantez_open.reverse()
print(parantez_open)

parantezs = []
for index, i in enumerate(parantez_open):
    while True:
        if i > parantez_close[index]:
            parantezs.append([i, parantez_close[index]])
            break
        else:
            index += 1

print(parantezs)
        
        
