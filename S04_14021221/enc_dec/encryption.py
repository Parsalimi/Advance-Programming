def encryption(entry_text):
    output = ""
    for char in list(entry_text):
        output += chr(ord(char) + 3)
    return output

