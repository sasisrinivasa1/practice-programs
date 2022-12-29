class School: # Class
    schoolname = "FinnLee HR School"

    def __init__(self,age, standard, section, rollno): # Paramterised Constructor
        self.age = age
        self.standard = standard
        self.section = section
        self.rollno = rollno
    def favsport(self,sport,name): 
        self.sport = sport
        self.name = name
        print(self.name + "'s Favourite Sport is " + self.sport)

#Object instantiation
charlie = School(14, 9, "B", 8) # charlie is an Object

guna = School(17, 12, "D", 21) # guna is an Object

revi = School(15, 10, "A", 34) # revi is an Object

print("What is the Charlie's Age? :: " + "Charlie's Age is " + str(charlie.age))
print("What is charlie's favourite sport? :: ",end="")
charlie.favsport("Hockey","Charlie")
print("What is the Guna's Standard? :: " + "Guna's Standard is " + str(guna.standard))
print("What is the Guna's Section? :: " + "Guna's Section is " + guna.section)
print("What is the Revi's Roll Number? :: " + "Revi's Roll Number is " + str(revi.rollno))
print("What is the Revi's Section? :: " + "Revi's Section is " + revi.section)

# Output:-
# PS C:\Users\Sasikumar S\Documents\python\practice-programs\oOP's> python .\objects_and_classes.py
# What is the Charlie's Age? :: Charlie's Age is 14
# What is charlie's favourite sport? :: Charlie's Favourite Sport is Hockey
# What is the Guna's Standard? :: Guna's Standard is 12
# What is the Guna's Section? :: Guna's Section is D
# What is the Revi's Roll Number? :: Revi's Roll Number is 34
# What is the Revi's Section? :: Revi's Section is A