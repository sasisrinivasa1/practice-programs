# Exception Handling
# ZeroDivisionError Exception
try:
    num1 = 12
    num2 = int(input("Enter the number for division :: ")) # Zero cannot be division by any numbers
    result = num1/num2
except ZeroDivisionError as ze:
    print("ZeroDivisionError :: " + str(ze))

#TypeError Exception
try:
    num3 = 3
    num4 = input("Enter the value for addition :: ") # input will get only by string type
    sum = num3 + num4
except TypeError as te:
    print("TypeError :: " + str(te))

#ValueType Error
try:
    num5 = 12
    num6 = int(input("Enter Number to subtract :: "))
    sub = num5 - num6
except ValueError as ve:
    print("Value Error :: " + str(ve))

# Multiple Exception Errors
try:
    num7 = 12
    num8 = input("Enter the Number :: ")
    output = num7/num8
    print("Output: :" + output)
except (ValueError,TypeError,ZeroDivisionError) as me:
    print("Multiple Exception Errors :: " + str(me))
