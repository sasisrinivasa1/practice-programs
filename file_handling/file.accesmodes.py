file = (open("xxx.txt","w"))
file.write("Hi..! How are you?")
file.close()

# Clearing the contents in files

file1 = open("abc.txt","w+") # Clear the contents in file
file1.close()

# Using x,x+ will not create the file again if its already created 
try:
    file2 = open("abcd.txt","x+")
    file2.write("x,x+ mode MUST not create the file again if its already created and it won't overwrite the existing file")
    file2.close()
except FileExistsError as fe:
    print("FileExistsError :: " + str(fe))

# Using r,r+ must create the file again if its already created and overwrites the content in file
file3 = open("abc.txt","r+")
file3.write("r,r+ must create the file again if its already created and overwrites the contents in file")
file3.close()

# Using w,w+ will clear the contents in the existing files
print("Clearing the xxx.txt file contents...")
file4 = open("xxx.txt","w+")
file.close()
print("Cleared the xxx.txt file contents.")

# Using a,a+ will append the files to the existing files
file5 = open("abcd.txt","a+")
print("Appending the extra contents to the abcd.txt file...")
file5.write("\na,a+ will append the files to the existing files")
print("Added the extra contents to the file.")
file5.close()