custom = ['llll','MM','122','765','UuUuU','78751','J']
numbers = ['100','200','300','250','45','89','10','9']

def sort(num):
    numbers.sort()
    num = numbers
    return num

sort_with_len = sorted(custom,key=len)
print(sort_with_len)
sort_with_str = sorted(custom,key=str)
print(sort_with_str)
sort_with_int = sorted(numbers,key=sort)
print(sort_with_int)

# Output:-
# ['J', 'MM', '122', '765', 'llll', 'UuUuU', '78751']
# ['122', '765', '78751', 'J', 'MM', 'UuUuU', 'llll']
# ['100', '200', '300', '250', '45', '89', '10', '9']