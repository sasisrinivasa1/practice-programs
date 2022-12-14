# sample-1
car = {'name':'magnite', 'age':3, 'seats':5, 'wheels':4}
car['gears'] = 6
print(car)
print(car['name'])

# sample-2
marks = {}
marks['Ram'] = 89
marks['Hassan'] = 67
marks['Kiran'] = 47
marks['Sandhiya'] = 80
print(marks)

for key in marks.keys():
    if marks[key] >= 70:
        print("The marks of", key, "is", marks[key])

for value in marks.values():
    print(value)

for key,value in marks.items():
    print(key,value)

# Output:-

# {'name': 'magnite', 'age': 3, 'seats': 5, 'wheels': 4, 'gears': 6}
# magnite
# {'Ram': 89, 'Hassan': 67, 'Kiran': 47, 'Sandhiya': 80}
# The marks of  Ram is 89
# The marks of  Sandhiya is 80
# 89
# 67
# 47
# 80
# Ram 89
# Hassan 67
# Kiran 47
# Sandhiya 80