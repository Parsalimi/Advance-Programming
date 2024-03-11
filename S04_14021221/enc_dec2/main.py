import random

list_space = [' ']
list_lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list_uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list_number = ['0','1','2','3','4','5','6','7','8','9']
list_special = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '[', ']', '{', '}', '|', '/', '.', ',', '<', '>', '?']
list_encryption = []

def set1():
    random_type = random.randint(1, 5)
    if random_type == 1:
        return list_space
    elif random_type == 2:
        return list_lowercase
    elif random_type == 3:
        return list_uppercase
    elif random_type == 4:
        return list_number
    elif random_type == 5:
        return list_special
    
entry = input("Enter: ")
entry_list = list(entry)
for i in range(0, len(entry)):
    list_encryption.append(random.choice(set1()))

print("".join(list_encryption))

entry_q = input("Enter: ")
for char in list(entry_q):
    for index, char1 in enumerate(list(list_encryption)):
        if char1 == char:
            print(entry_list[index],end="")
