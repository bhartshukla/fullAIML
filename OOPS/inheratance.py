# inheritance --- Reusing attr and methods from a parent (Base) class

class employee:
    start_time = "10 AM"
    end_time = "5 PM"

    def chnage_time(self, new_chnage_time):
        self.end_time = new_chnage_time

class teacher(employee):
    def __init__(self, subject):
        self.subject = subject


class Admin(employee):
    def __init__(self, role):
       self.role = role


p1 = Admin("CEO")
# print(p1.role, p1.end_time)



t1  = teacher("MATH") 

# print(t1.subject, t1.start_time)

t1.chnage_time("6pm")
# print(t1.end_time)


# types of inheritance ---------
# 1) single level inheritance --
# 2) multi level inheritance --
# 3) multiple inheritance --

class employee:
    start_time = "10 AM"
    end_time = "5 PM"

class Admin(employee):
    def __init__(self, role):
       self.role = role

class acountant(Admin):
    def __init__(self, salary, role):
        super().__init__(role)  # its method to invoke oue Upper class attributes 
        self.salary = salary
        

p1 = acountant(40000, "CA")
# print(p1.salary, p1.end_time)





# 3) multiple inheritance --

class Teacher:
    def __init__(self,salary):
        self.salary = salary


class student:
    def __init__(self, gpa):
        self.gpa = gpa

class TA(Teacher, student) :
    def __init__(self, salary, gpa, name):
        super().__init__(salary)      
        student.__init__(self,gpa) 
        self.name = name

tal = TA(15000, 9.6, "BHARAT")

print(tal.name,tal.salary, tal.gpa)