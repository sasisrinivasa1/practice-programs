import sys
cars = ['Suzuki','Nissan','Renault','Benz','BMW']
i=0
while (i<=len(cars)):
    if (cars[i] == sys.argv[1]):
        print("My Favorite car is", cars[i])
        print("My favorite car's index is", cars.index(sys.argv[1]))
        break
    else: 
        i += 1
        continue

# Output:

# python .\while_loop.py BMW
# My Favorite car is BMW
# My favorite car's index is 4