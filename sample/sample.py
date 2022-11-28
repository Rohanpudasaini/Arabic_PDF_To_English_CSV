import os
os.chdir("Documents/")
l = os.listdir()
for item in l:
    a = os.path.splitext(item)
    print(a)