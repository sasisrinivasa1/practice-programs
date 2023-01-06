from collections import ChainMap
# import collections

dict_1 = {'a':87,'b':88,'c':89}
dict_2 = {'d':90,'e':91,'f':92}
dict_3 = {'g':93}
dict_4 = {'i':56,'j':76}

dictt = ChainMap(dict_3,dict_1,dict_2) # Chain Map will combine the dict1,dict2,dict3
# dictt = collections.ChainMap(dict_3,dict_1,dict_2)
print(dictt)

#maps()
print(dictt.maps) # maps will stores it in Single Array.
for i in dictt.maps:
    print(i)

#keys() & values()
print("Printing the keys in list :: ", list(dictt.keys()))
print("Printing the values in list :: ", list(dictt.values()))

#new_child() also will add the dictionary
dictt1 = dictt.new_child(dict_4)
print(dictt1)