# X = open(address,defult 'r')
# w: write -> delete first and write afterward
# r: read
# a: append
# x: create -> create a file 
# X.close

x = open("text.txt")
#print(x.read(12))
#print(x.readline(50)) # only the first line
for line in x:
    print(line)
x.close

try:
    pass
except:
    pass
finally:
    pass
with open("text.txt","r") as f:
    pass

import os
if not os.path.exist("text.txt"):
    f = open("text.txt",'x')