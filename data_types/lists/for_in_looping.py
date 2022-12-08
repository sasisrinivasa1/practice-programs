numbers1 = [100,200,300,150,125,75,50]
numbers2 = ["One ","Two ","Three ","Four "]

# Sample-1
def subtract(num):
    sub = 36
    sub += num
    return sub

print("Output of Sample-1:-")
for num in numbers1:
    subtract(num)
    print("Subtracting the", num, "by 36 is", subtract(num))

# Sample-2
print("\nOutput of Sample-2:-")
concat = "Zero "
for string in numbers2:
    concat += string
    print(concat)

# Output of Sample-1:-
# Subtracting the 100 by 36 is 136
# Subtracting the 200 by 36 is 236
# Subtracting the 300 by 36 is 336
# Subtracting the 150 by 36 is 186
# Subtracting the 125 by 36 is 161
# Subtracting the 75 by 36 is 111
# Subtracting the 50 by 36 is 86

# Output of Sample-2:-
# Zero One
# Zero One Two
# Zero One Two Three
# Zero One Two Three Four