class myError(RuntimeError):
    def __init__(self,city):
        self.city = city
try:
    raise myError("Bangalore") # user-defined exception raised
except myError as error:
    print("My City is " + error.city)