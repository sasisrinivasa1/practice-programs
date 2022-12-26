def fib(num):
    num1 = 0
    print(num1,end=' ')
    num2 = 1
    print(num2,end=' ')
    for i in range(2,num+1):
        num3 = num1 + num2
        print(num3,end=' ')
        num1 = num2
        num2 = num3

def factorial(num):
    if num > 0:
        result = 1
        for i in range(1, num+1):
            result = result * i
        print("The Factorial of " + str(num) + " is " + str(result))
    else: print("Factorial of Zero is 1")

def primeNum(num):
    if num == 0:
        print("Zero is not an Prime Number, it is divisible by 1")
    if num == 1:
        print(str(num) + " is a Prime Number")
    if num == 2:
        print(str(num) + " is not a Prime Number")
    if num > 2:
        for i in range(2,num):
            if num % i == 0:
                print(str(num) + " is not a Prime Number, it is divisible by " + str(i))
                isPrime = False
                break
            else:
                isPrime = True
        if isPrime == True:
            print(str(num) + " is a Prime Number, it is divisble by only " + str(num)) 

def add(a,b):
    print("Addition of Two number is " + str(a+b))

def subtract(a,b):
    print("Subtraction of Two number is " + str(a-b))

def mul(a,b):
    print("Multiplication of Two number is " + str(a*b))

def divide(a,b):
    print("Division of Two number is " + str(a/b))

def myName(name):
    print("My Name is " + name)

def myCity(city):
    print("My City is " + city)

def laptop(brand):
    print("My Laptop's company is " + brand)