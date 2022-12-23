# using else in exception's
try:
    num1 = 10
    num2 = int(input('Enter the number: :'))
    result = num1 + num2
except ValueError as ve:
    print("ValueError ::" + str(ve))
else:               # If try block got successful without any exceptions, else will execute
    print("Addition is successful")
    print(result)

# Output:-
### If try block got success ###
# Enter the number: :2
# Addition is successful
# 12

### If try block got Exception ###
# Enter the number: :x
# ValueError ::invalid literal for int() with base 10: 'x'