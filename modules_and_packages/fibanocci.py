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