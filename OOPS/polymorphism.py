# 1 - function overriding (its use when inheritance availabe) , redefinig parent class fnx in child class




class Employee:
    def get_deg(self):
       print("deg = Employee") 

class Teacher(Employee):
    def get_deg(self):
        print("deg = Teacher")

t1 = Teacher()
# t1.get_deg()      


# 2 - duck typing (walks like a duck and quaks liks a duck)

class Teacher():
    def get_deg(self):
        print("deg = Teacher")

class Accountant():
    def get_deg(self):
        print("deg = Accountant")   

        
             