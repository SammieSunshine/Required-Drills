#
#   Python ver. 3.8.5
#
#   Author: Samantha Billips
#
#
#   Assignment 224: Create a class that utilizes the concept of abstraction
#
#


#Class should contain at least one ABSTRACT method and one REGULAR method



# Abstract Method
from abc import ABC, abstractmethod
class Zoo(ABC):
    def Giraffe(self, amount):
        print("There are {} Giraffes in this zoo.".format(amount))

        @abstractmethod
        def Animal(self, amount):
            pass

class Animal(Zoo):
    def Zebra(self, amount):
        print('Number of Zebras in the zoo: {}'.format(amount))

obj = Animal()
obj.Giraffe("10")
obj.Zebra("15")




# Regular Method
#parent
class Zoo2: 
    def __init__(self,name):
        self.__name = name

    def getInfo(self):
        return self.__name

#child/ references parent in parenthesis
class Animals(Zoo2): 
    def getAnimalInfo(self):
        #calls getinfo from Parent
        return 'Animal: ' + Zoo2.getInfo(self)

animal = Animals('Giraffe')
print(animal.getAnimalInfo())
    
    
        

    
