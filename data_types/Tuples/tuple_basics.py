day = ('monday','tuesday','wednesday','thursday','friday')
print(day)
print(day[0])

# day[2] = 'sunday' # tuple 'day' is immutable
day = ('January','Febraruy','March','April','May') # we can change the entire tuple values
print(day)
print(len(day))
print(sorted(day))
print(day[4])

(google, visual, music) = ('chrome','studio','player')
print(google)

# Output:-
# ('monday', 'tuesday', 'wednesday', 'thursday', 'friday')
# monday
# ('January', 'Febraruy', 'March', 'April', 'May')
# 5
# ['April', 'Febraruy', 'January', 'March', 'May']
# May
# chrome