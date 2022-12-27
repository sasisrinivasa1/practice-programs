import sys

# class
class Apartment_Details():
    # common variables
    apartment_name = "Valencia Creations"

    # instance_variables, contructs the value to the variables
    def __init__ (self, name, flat_number, location):
        self.owner_name = name
        self.flat_number = flat_number
        self.location = location

    # normal definition
    def ageofBuilding(self, age):
        print("The Apartment " + self.apartment_name + "is " + str(age) + " years old which is in " + self.location )

def owner_details():
    owner_1 = Apartment_Details("Akash", "A4-304", "Egattur")
    print("Owner_1 Name:- ", owner_1.owner_name)
    print("Owner_1 Location:- ", owner_1.location)
    owner_2 = Apartment_Details("Hari", "D-90", "Padur")
    print("Owner_2 Location:- ", owner_2.location)
    print("Owner_2 Apartment Name:- ", owner_2.apartment_name)
    owner_3 = Apartment_Details("Sharan", "S-45", "Navalur")
    print("Owner_3 Name:- ", owner_1.owner_name)
    print("Owner_3 Location:- ", owner_3.location)
    print("Owner_3 FlatName:- ", owner_1.flat_number)
    owner_1.ageofBuilding(20)

if __name__ == "__main__": # predefined main function
    owner_details()

# OUTPUT:-

# Owner_1 Name:-  Akash
# Owner_1 Location:-  Egattur
# Owner_2 Location:-  Padur
# Owner_2 Apartment Name:-  Valencia Creations
# Owner_3 Name:-  Akash
# Owner_3 Location:-  Navalur
# Owner_3 FlatName:-  A4-304
# The Apartment Valencia Creationsis 20 years old which is in Egattur