# deleting the list or dictionary in the object

dict = {'a':99,'b':87,'c':90,'d':78}
print(dict)
print("Deleting the 'd' dictionary element....")
del dict['d']
print("Deleted the 'd' element")
print(dict)

print(".."*30)
list = [12,23,34,54,10,9,75,12983,4374,918,90]
print(len(list))
print("Deleting the list elements from the range of 2 to 6...")
del list[2:7]
print("Deleted the list elements of range 2 to 6")
print(list)

# Output:-
# PS C:\Users\Sasikumar S\Documents\python\practice-programs\data_types\Dictionary> python .\delete.py
# {'a': 99, 'b': 87, 'c': 90, 'd': 78}
# Deleting the 'd' dictionary element....
# Deleted the 'd' element
# {'a': 99, 'b': 87, 'c': 90}
# ............................................................
# 11
# Deleting the list elements from the range of 2 to 6...
# Deleted the list elements of range 2 to 6
# [12, 23, 12983, 4374, 918, 90]