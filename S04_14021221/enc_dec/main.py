import encryption as e
import decryption as d
from os import system

enter = input("Enter: ")
result = e.encryption(enter)

while True:
    system('cls')
    print(result)
    enter = input("Enter: ")
    print(d.decryption(enter))
    input("press enter to continue")