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