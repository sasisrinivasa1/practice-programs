# finally will surely execute his block if there is an exception or not
try:
    fh = open("Sample.txt", "r")
    fh.write("Hello Python")
except IOError:
    print("File is not in write mode")
finally:
    fh.close()
    print("File Closed successfully")