from os import system
from math import floor


# def isPolindrome(word):
#     if word.lower() == (word[::-1]).lower():
#         return True
#     else:
#         return False


def isPolindrome(word):
    correct = 0
    if len(word) % 2 == 0:
        for i in range(0, len(word)/2):
            if word[i] == word[len(word) - 1 - i]:
                correct += 1
        if correct == len(word):
            return True
        else:
            return False
    else:
        for i in range(0, floor(len(word)/2)):
            if word[i] == word[len(word) -1 - i]:
                correct += 1
        if correct == len(word):
            return True
        else:
            return False


flag = True
while flag:
    system('cls')
    answer = input('0. To Quit\nEnter a word to check: ')
    if answer == "0":
        flag = False
    else:
        print(answer[::-1])
        print(isPolindrome(answer))
        input("Press Enter to Continue!!!")
