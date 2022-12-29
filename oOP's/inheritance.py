class Base_1(object):
    def __init__(self,location,name):
        self.location = location
        self.name = name
class Derived_1(Base_1):      # Inherited the Base_1 Class properoties to Derived_1 Class
    def __init__(self,storeid,postcode,street,storemailid,storecontact,location,name):
        self.storeid = storeid
        self.street = street
        self.postcode = postcode
        self.storemailid = storemailid
        self.storecontact = storecontact

        Base_1.__init__(self,location,name)

storelocation = Base_1("Nottingham","Swiggy-Mart")
store_details = Derived_1(2031,600021,"Sterland Street","SwiggyInstamart@gmail.com",9876544321,"Nottingham","Swiggy-Mart")

print(store_details.name + " is biggest grocery market in " + store_details.location + ".")
print("Store Address :: StoreID: " + str(store_details.storeid) + ", " + store_details.street + ", " + store_details.location + "-" + str(store_details.postcode))
print("Contact Swiggy store by \nmailid :: " + store_details.storemailid + '\n' + "contact :: " + str(store_details.storecontact))

# Output:-

# PS C:\Users\Sasikumar S\Documents\python\practice-programs\oOP's> python .\inheritance.py
# Swiggy-Mart is biggest grocery market in Nottingham.
# Store Address :: StoreID: 2031, Sterland Street, Nottingham-600021
# Contact Swiggy store by 
# mailid :: SwiggyInstamart@gmail.com
# contact :: 9876544321