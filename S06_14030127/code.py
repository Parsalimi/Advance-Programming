import os
with open("file1.txt","w") as f1_w:
    f1_w.write("Write this text just for test!!!")
    f1_w.close()

with open("file2.txt","w") as f2_w:
    with open("file1.txt","r") as f1_r:
        f2_w.write(f1_r.read())
        f1_r.close()
        f2_w.close()
        os.remove("file1.txt")