text1 = "-Python-Programming-Language-"
value1 = " $ "
value2 = "_"
name1 = '-'

# convert from upper case to lower case
print("Lower Case string:- ", text1.lower(), "\n")

# convert from lower case to upper case
print("Upper Case string:- ", text1.upper(), "\n")

# split the string
print("Split the text1 string:- ", text1.split('-'), "\n")
result = text1.split(name1)

# join the string
print("Joining the splitted string:- ", value1.join(result), '\n')

# checking starts with and end with object 
string = value2.join(result)
print("Is string starts with 'python' ? - ", string.startswith('python'))
print("Is string starts with '_python' ? - ", string.startswith('_python'))
print("Is string starts with '_Python' ? - ", string.startswith('_Python'))
print("Is string ends with 'Language' ? - ", string.endswith('Language'))
print("Is string ends with 'Language_' ? - ", string.endswith('Language_'), "\n")

# printing the center strings
print("String in between of 50's :- ", string.center(50), "\n")

# finding the String
findString = ['gramming','Gramming','_Python_']
for value3 in findString:
    if (string.find(value3) == -1):
        print("The string '", value3, "' doesn't exists")
    else:
        print("The string '", value3, "' exists in Index of", string.find(value3))

# Replacing the string
print("\nReplacing the Python string with Java:- ", string.replace('Python','Java'), "\n")

# Check classes of string
alphabets = 'abcdef'
num = ["1","2","3"]
print("Check the String classes")
print(string.isalpha())
print(alphabets.isalpha())
print(num[2].isdigit())

# OUTPUT:-

# Lower Case string:-  -python-programming-language- 

# Upper Case string:-  -PYTHON-PROGRAMMING-LANGUAGE-

# Split the text1 string:-  ['', 'Python', 'Programming', 'Language', '']

# Joining the splitted string:-   $ Python $ Programming $ Language $

# Is string starts with 'python' ? -  False
# Is string starts with '_python' ? -  False
# Is string starts with '_Python' ? -  True
# Is string ends with 'Language' ? -  False
# Is string ends with 'Language_' ? -  True

# String in between of 50's :-            _Python_Programming_Language_

# The string ' gramming ' exists in Index of 11
# The string ' Gramming ' doesn't exists
# The string ' _Python_ ' exists in Index of 0

# Replacing the Python string with Java:-  _Java_Programming_Language_

# Check the String classes
# False
# True
# True