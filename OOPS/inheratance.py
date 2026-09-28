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
print(p1.role, p1.end_time)



t1  = teacher("MATH") 

print(t1.subject, t1.start_time)

t1.chnage_time("6pm")
print(t1.end_time)


