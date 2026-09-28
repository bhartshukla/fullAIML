# constructor -- a constructor is a special method that automatically runs when you create an object.

# __init__methd() -- this used for initialise our object

# def __init__(self):
#     print("this is the constuctor")

# self parameter -- storing current instance of the class
# -- reference of current object ,


# note --- one init methhod for per class, not diffrent defferent inits 

# object has higher priority its hass all property of class and object both 

class Student:
    def __init__(self): # default constructor
        pass
    def __init__(self, name, cgpa):  #Parameterizerd constructor
        # print("constructor was called ")
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa

stu1 = Student("Rahul", 9.0)       
stu2 = Student("Bharat" ,8.6)       
stu3 = Student("Shukla", 8.6)    

# print(stu1.name, stu1.cgpa)
# print(stu2.name)
# print(stu3.name)

# print(stu2.get_cgpa())


# type of constructor ---------
# default -- only self parameter (one parameter)
# Parameterizerd -- self + another parameter 


# Attributes in OOPS PYTHON
# 1 - class --   these belong to class -- common
# 2 - Instance -- these belong to Object -- unique/ diff


class STUD:
    coll_name = "ABC_COLLEGE" # its common for all student so its class Attributes 

    def __init__(self, name , gpa):
        self.name = name  # its diff for all student so its intance attributes
        self.gpa = gpa  # its diff for all student so its intance attributes


st1 = STUD("Bharat" , 9.2)

# print(st1.gpa)



# Methods in OOPS python Class
# 1- Instance - this method access all attributes (intance and class both) and its first parameter is self its only called unsing object name



# 2- class -- its first parameter is cls, its access on class Attributes not Isntance attributes and also use decorator which is class decorator ("@classmethod") this method called also with class name and object name both its only access class cls attributes 




# 3- Static metjod --  no any compalsory parameter , these cnat accsess instance attributes or not class attributes , for this we use a decorator which is staticmethod , these logicly tideup with class 



class laptop:
    storage_type = "SSD"

    @classmethod  # class decoratore
    def get_storage(cls): # its a clas method
        print(f"laptop storage type is {cls.storage_type}")


    def __init__(self, ram , storage):
        self.ram = ram
        self.storage = storage



    def getInfo(self): # instance Method
        print(f"the ram of latptop is {self.ram} and storage is {self.storage} and storage type is {self.storage_type}")

    @staticmethod
    def get_price(price, discount):
        finalprice = price-(discount*price/100)
        print(f"the final price of laptop is {finalprice}")



l1 = laptop("16gb", "512gb" )

# print(l1.getInfo()) 
# l1.get_storage()

# l1.get_price(40_000, 10)





# question 

class store:
    count  = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        store.count += 1

    def get_info(self): # instace method 
        print(f"the pric of product is {self.price} and the product name is {self.name}")   

    @classmethod
    def totalobj(cls):
        print(f"total product is = {cls.count}")

    

    

p1 = store("Mobile", 20000)
p2 = store("Laptop", 40000)
p3 = store("PC", 50000)

p1.get_info()         

store.totalobj()