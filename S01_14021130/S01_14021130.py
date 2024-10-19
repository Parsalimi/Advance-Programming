# Project - Phase 1
from os import system
flag = True
min = 0
new_list = []
entered_list = []
Integear = True


def func_sort(entery_list):
    for j in range(0, len(entery_list) - 1):
        for i in range(0, len(entery_list) - 1):
            if entery_list[i] > entery_list[i+1]:
                a = entery_list[i]
                b = entery_list[i+1]
                entery_list[i+1] = a
                entery_list[i] = b
    return entered_list

func_sort([3,5,1,10])







def fun_stack_sort(entery_list):
    for i in range(0, len(entery_list) - 1):
        min = entered_list[0]
        for j in range(0, len(entery_list)):
            if entery_list[j] < min:
                min = entery_list[j]
        new_list.append(min)
        entered_list.remove(min)
    new_list.append(entery_list[0])
    
    return new_list

while flag:
    system("cls")
    new_list = []
    entered_list = []
    count = int(input("How many numbers do you want to enter: "))
    for i in range(0, count):
        system('cls')
        try:
            entered_num = int(input("Please enter the number: ")) 
        except ValueError:
            entered_num = int(input("Please enter an integear\nPlease enter the number: "))
        entered_list.append(entered_num)

    while True:
        system("cls")
        print(f"Entered List is: {entered_list}")
        answer = input("1. Stack-way\n2. Normal-way\nEnter: ")
        if answer == "1":
            print(fun_stack_sort(entered_list))
            input("To continue press enter")
            break
        elif answer == "2":
            print(func_sort(entered_list))
            input("To continue press enter")
            break
        else:
            input("Please give me a valid answer!\nTo continue Press Enter")

    while True:
        system("cls")
        answer = input("Do you want to continue? (yes/no): ")
        if answer == "no":
            flag = False
            break
        elif answer == "yes":
            break
        else:
            input("Please give me a valid answer!\nTo continue Press Enter")
