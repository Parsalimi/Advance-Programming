solid_entry = '(23+40)x23'
myList = []
looking_list = ['(',')','+','-','x','/']
last_important_index = 0

for index, char in enumerate(solid_entry):
    if char in looking_list:
        if index > 0:
            myList.append(solid_entry[last_important_index+1:index])
            myList.append(char)
            last_important_index = index
        else:
            myList.append(char)

myList.append(solid_entry[last_important_index+1:len(solid_entry)]) # append the last 

for item in myList:
    if item == '':
        myList.remove(item)
print(myList)