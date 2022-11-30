import sys

# Simple string repeat program
name = "String_Repeat "
value = 5
get = name * value
print("Output-1:- ", get)

word = sys.argv[1]
print("Output-2:", end= "- ")
print(word * int(sys.argv[2]))

# Program using definition calling from predefined main function
def repeat_string(word1, value1):
    Result = (word1 * int(value1))
    return Result

if __name__ == "__main__":
    Result = repeat_string(sys.argv[3], sys.argv[4])
    print("Output-3:-", Result)

## OUTPUT:-
# python .\strings.py "Hello " 3 "World_Repeat " 4
# Output-1:- String_Repeat String_Repeat String_Repeat String_Repeat String_Repeat 
# Output-2:- Hello Hello Hello 
# Output-3:- World_Repeat World_Repeat World_Repeat World_Repeat

