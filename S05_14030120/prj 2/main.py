from os import system

def khayam_pascal(lenght):
    if lenght == 0:
        return [0]
    
    real_lenght = 1
    old_Eq = []
    while real_lenght <= lenght:
        main_Eq = []
        for i in range(0, real_lenght+1):
            main_Eq.append(0) 

        main_Eq[0] = 1
        main_Eq[len(main_Eq)-1] = 1
        
        if real_lenght > 1:
            for j in range(1, len(main_Eq)-1):
                main_Eq[j] = old_Eq[j-1] + old_Eq[j]

        old_Eq = main_Eq 
        real_lenght+=1
        



    return old_Eq

system('cls')
entry = int(input("Please enter a number that you want: "))
print(khayam_pascal(entry))