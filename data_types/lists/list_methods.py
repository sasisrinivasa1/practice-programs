os = []
lap_brands = ["Dell","Lenovo","HP","Acer"]

# append() will add any datatype value in list
os.append("Windows")
print(os)
os.append("Ubuntu")

# inserting any datatype value in the list
os.insert(1,"Linux")
print(os)

# extend() will add to old list
os.extend(lap_brands)
print(os)

# searches the index element in the list
print(os.index("Ubuntu"))
print(os.index("HP"))

# removing the element in list
os.remove("Acer")
print(os)

# sorting the elements in lists
os.sort()
print(os)

# reverse the sorting elements in list
os.reverse()
print(os)

# pop() - removes and returns the item
print(os.pop(4))
print(os)

# OUTPUT:-

# ['Windows']
# ['Windows', 'Linux', 'Ubuntu']
# ['Windows', 'Linux', 'Ubuntu', 'Dell', 'Lenovo', 'HP', 'Acer']
# 2
# 5
# ['Windows', 'Linux', 'Ubuntu', 'Dell', 'Lenovo', 'HP']
# ['Dell', 'HP', 'Lenovo', 'Linux', 'Ubuntu', 'Windows']
# ['Windows', 'Ubuntu', 'Linux', 'Lenovo', 'HP', 'Dell']
# HP
# ['Windows', 'Ubuntu', 'Linux', 'Lenovo', 'Dell']