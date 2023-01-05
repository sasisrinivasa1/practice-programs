import os

# getcwd() is to get Current Working Directory
cwd = os.getcwd()
print(cwd)

# creating the directory
try:
    crdir = os.path.join(cwd,"newDirectory")
    print("Creating the new Directory...")
    os.mkdir(crdir)
    print("Created the new Directory")
except FileExistsError as er:
    print(str(er))

# changing to other directory
os.chdir(crdir)
print("Current Working Directory :: ", os.getcwd())

# creating the new file in new Directory folder
try:
    open("hello.txt","x+")
except FileExistsError:
    print("Hello.txt File Already exists..")
file = open("file1.txt","w+")
file.write("Hello Welcome to file1..")
file.close()
file = open("file1.txt","a")
file.write("\nAdding the new line")
file.close()

# list files in the directory

print(os.listdir(os.getcwd()))