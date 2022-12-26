file = open("sample1.txt","r")
print(file)
count = 0
for i in file:
    print(file.read(6))
    print(i,end='')