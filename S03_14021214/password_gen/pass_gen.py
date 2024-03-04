import string
import random
from random import randint

def password_generator():
    pass_len = 8
    password = []
    main_pass = []

    num_count = randint(0,8)
    for i in range(0, num_count):
        password.append(str(randint(0,9)))
    letter_count = pass_len - num_count
    for i in range(0, letter_count):
        randomLetter = random.choice(string.ascii_letters)
        password.append(randomLetter)

    for i in range(0, pass_len):
        char = random.choice(password)
        main_pass.append(char)
        password.remove(char)

    return "".join(main_pass)