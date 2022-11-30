import sys

# Simple string repeat program
name = "String_Repeat "
value1 = 5
get = name * value1
print("Output-1:- ", get)
print("\n")

word = sys.argv[1]
print("Output-2:", end= "- ")
print(word * int(sys.argv[2]))
print("\n")

# string concat
word1 = "Debug "
text1 = "Console"
print("Output-3:- ", word1 + text1)
print("\n")

# Program using definition calling from predefined main function
def repeat_string(word2, value2):
    Result = (word2 * int(value2))
    return Result

if __name__ == "__main__":
    Result = repeat_string(sys.argv[3], sys.argv[4])
    print("Output-4:-", Result)


# OUTPUT:- 
# python .\strings.py "Hello " 3 "World_Repeat " 4
# Output-1:-  String_Repeat String_Repeat String_Repeat String_Repeat String_Repeat 

# Output-2:- Hello Hello Hello 

# Output-3:-  Debug Console

# Output-4:- World_Repeat World_Repeat World_Repeat World_Repeat

