numbers = [1,10,30,230,200,20,113,560,600,60]
names = ['qwerty', 'asdfgh','zxcvbn','poiu','lkj','m']

# sorted() method is a temporary sorting, doesnt overrides the original stored memory
sorted_names = sorted(names)
print("Print numbers in Ascending order", sorted(numbers))
print("Print numbers in Descending order", sorted(numbers, reverse=True))
print("Print names in Descending order", sorted(names, reverse=True))
print(names) # The names list will not be change

# sort() and reverse() is a function, which override the original memory
print("\n=================================\n")
names.sort()
print("Print names in Ascending order by using sort() function..", names)
names.reverse()
print("Print names in Descending order by using reverse() fuction..", names)

# Output:-
# ['asdfgh', 'lkj', 'm', 'poiu', 'qwerty', 'zxcvbn']
# Print numbers in Ascending order [1, 10, 20, 30, 60, 113, 200, 230, 560, 600]
# Print numbers in Descending order [600, 560, 230, 200, 113, 60, 30, 20, 10, 1]
# Print names in Descending order ['zxcvbn', 'qwerty', 'poiu', 'm', 'lkj', 'asdfgh']
# ['qwerty', 'asdfgh', 'zxcvbn', 'poiu', 'lkj', 'm']

# =================================

# Print names in Ascending order by using sort() function.. ['asdfgh', 'lkj', 'm', 'poiu', 'qwerty', 'zxcvbn']
# Print names in Descending order by using reverse() fuction.. ['zxcvbn', 'qwerty', 'poiu', 'm', 'lkj', 'asdfgh']