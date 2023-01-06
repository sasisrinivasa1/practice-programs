from collections import namedtuple
# import collections

# Declaring the namedtuple()
S = namedtuple('Person',['name','age','cardnumber'])
obj = S("Arjun",20,98493284)
print(obj.cardnumber)
print(obj[0])
print(obj)

new = ('Aari',23,97986982)
# using _make() function
obj1 = S._make(new)
print(obj1.name)
print(obj1[1])

#using asdict() function
print(obj._asdict())

# using fields() function
print(obj1._fields) # This will print the fields 

# using replace function
print(obj1._replace(cardnumber=1224343))