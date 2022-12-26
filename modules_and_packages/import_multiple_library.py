import sys
import factorial
import fibanocci
import prime_number

if __name__ == '__main__':
    num = int(sys.argv[1])
    print('-'*50)
    factorial.factorial(num)
    print('-'*50)
    prime_number.primeNum(num)
    print('-'*50)
    fibanocci.fib(num)
    
# Output:-
# PS C:\Users\Sasikumar S\Documents\python\practice-programs\modules_and_packages> python .\import_multiple_library.py 21
# --------------------------------------------------
# The Factorial of 21 is 51090942171709440000
# --------------------------------------------------
# 21 is not a Prime Number, it is divisible by 3
# --------------------------------------------------
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946