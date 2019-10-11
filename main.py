import os

f = open('ext.txt', 'r')
extList = f.readlines()
dirList = []
for d in os.listdir('./'):
    if os.path.isdir(d):
        dirList.append(d)

print(dirList)
