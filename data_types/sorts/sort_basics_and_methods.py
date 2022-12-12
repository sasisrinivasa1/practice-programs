numbers = [2,30,10,22,45,54,53,21,100,300,44,87]
string = ['aa','Aa','bbb','zxc','zcb','Ecb','Seb']
characters = ['U','E','e','w','Z','b','h']

descend_numbers = sorted(numbers,reverse= True)
ascend_string = sorted(numbers,reverse=False)
ascend_character = characters.sort() # sort() is not an return type. It returns None

print(descend_numbers)
print(ascend_string)
print(ascend_character)

characters.sort()
print(characters) # return the characters with sorting