def factorial(num):
    if num > 0:
        result = 1
        for i in range(1, num+1):
            result = result * i
        print("The Factorial of " + str(num) + " is " + str(result))
    else: print("Factorial of Zero is 1")