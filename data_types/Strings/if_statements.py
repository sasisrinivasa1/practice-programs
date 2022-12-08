def mobile(brand):
    print("The Brand is ", brand)

brands = "Samsung"

if brands.find("oneplus") == -1:
    mobile("OnePlus")
    if brands.find("Samsung") != -1:
        mobile("Samsung")
    else: 
        print("No brands found")
else: print("No brands found")