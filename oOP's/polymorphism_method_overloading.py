class MyClass():

    def add(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        return self.a + self.b + self.c
    def add(self,a,b):
        self.a = a
        self.b = b
        return self.a + self.b

# Overloading will work for latest method defined inside the class

obj = MyClass()

# print(obj.add(2,3,5))
print(obj.add(2,3)) # Latest defined method will run by default