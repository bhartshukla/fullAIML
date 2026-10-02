
# ABSTRACTION -- Hiding internal details & Showing only essential freatures



# Abstract class - blueprint for other classes
#ABC module in python

# for makeing a abstract class or abstract method "from abc import ABC, abstractmethod"
    


from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar!")

class cow (Animal):
    def make_sound(self):
        print("maaaa!")        

lion  = Lion()
lion.make_sound()        


cow = cow()
cow.make_sound()
