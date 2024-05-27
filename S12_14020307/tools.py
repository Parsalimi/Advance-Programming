from os import system
from colorama import Fore

def ClearTerminal():
    system('cls')

def Wait():
    input("Press Enter to Continue!!!")

def ColoredNotification(text:str, color:str,) -> str:
    """
    :Arguments:
    :text - Enter whatever you want to write
    :color - you can choose your text color between 3 colors "red","green","cyan"

    :Return:
    :It returens your text with your requested color
    :⚠️ Dont forget to print it or use it in input func ⚠️
    """
    if color == "red":
        return (Fore.RED + text + Fore.WHITE)
    elif color == "green":
        return (Fore.GREEN + text + Fore.WHITE)
    elif color == "cyan":
        return (Fore.CYAN + text + Fore.WHITE)
    
def TextStructure(text, desired_width):
    remaining_space = desired_width - len(text)
    if remaining_space % 2 == 0:
        spaces_width = int(remaining_space / 2)
        return (spaces_width * ' ' + text + spaces_width * ' ')
    else:
        spaces_width = int(remaining_space // 2)
        return (spaces_width * ' ' + text + (spaces_width + 1) * ' ')
    
# def getEntry(question):
#     flag = True
#     while flag:
#         ClearTerminal()
#         answer = input(question)
#         if ',' in answer or '\\' in answer:
#             print(Fore.RED + "You can't use '\\' or ','" + Fore.WHITE)
#             Wait()
#         else:
#             break
        
#     return answer