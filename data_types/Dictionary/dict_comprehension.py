dict_1 = {'Sasi':90, 'Pavan':89, 'Jagan':85,'Priya':47, 'Ram':67, 'Revi':23,'Zaikr':58,'Yash':74, 'Udai':60}
dict_2 = {}

print("."*60)
print("DICTIONARY COMPREHENSION")
dict_2 = { key:value for key,value in dict_1.items() if value <= 59 }
print(dict_2)
print("."*60)

print("."*60)
print("DICTIONARY FORMATTING")
for key,value in dict_2.items():
    if value < 35:
        print(key + " has scored below 35 mark." + " His actual score is " + str(value))
print("."*60)

dict_1['Siri'] = 47
print(dict_1)

# OUTPUT:-
# PS C:\Users\Sasikumar S\Documents\python\practice-programs\data_types\Dictionary> python .\dict_comprehension.py
# ............................................................
# DICTIONARY COMPREHENSION
# {'Priya': 47, 'Revi': 23, 'Zaikr': 58}
# ............................................................
# ............................................................
# DICTIONARY FORMATTING
# Revi has scored below 35 mark. His actual score is 23
# ............................................................
# {'Sasi': 90, 'Pavan': 89, 'Jagan': 85, 'Priya': 47, 'Ram': 67, 'Revi': 23, 'Zaikr': 58, 'Yash': 74, 'Udai': 60, 'Siri': 47}    