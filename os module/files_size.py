import os

mypath = os.getcwd()
n = 10000

for root, dirs, files in os.walk(mypath):
    for f in files:
        fullpath = os.path.join(root, f)
        size = os.path.getsize(fullpath)
        if size >= n:
            print(f)
            print(size)
