def ishepassed(mark,name):
    assert (mark > 35), (name + " got " + str(mark) + " which is below 35. " + name + " is Failed")
    return (name + " got " + str(mark) + " which is above 35. " + name + " is Passed")

print(ishepassed(65,"John"))
print(ishepassed(43,"Arun"))
print(ishepassed(32,"Melin"))