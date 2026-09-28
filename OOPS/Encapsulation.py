# Encapsulation ------
# Wrapping data and function into single unit

# DATA HIDING ------------ in puthon data hiding by conveation 

# public -- inside class + outside class 
# protected -- class + subclasses 
# private --  inside the class one , use _ this for making protected and use __ for making private

# for access the private data use getter and setters methods


class BankAcc:
    def __init__(self,name , Balance , Password):
        self.name = name #public 
        self._Balance = Balance  # protected 
        self.__Password = Password # private - data mangling -- its not completly protected 

    def get_pass(self):  # getter function
        return self.__Password

    def set_pass(self, newpass):
        self.__Password = newpass

acc1 = BankAcc("Bharat", 100000, "bharat123")      

print(acc1.name)
print(acc1._Balance)
# print(acc1.__Password) # give error 

print(acc1._BankAcc__Password)  # access with this for private attributes 

print(acc1.get_pass())  ## accaes private 

acc1.set_pass("bharatashuj")

print(acc1.get_pass())
        





