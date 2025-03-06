#Getter, Setter, Private Variable

class Person:
    personCount = 0 # class variable
    def __init__(self, name, DoB, gender):
        #instance variables / object variables
        self.__name = name #__ to private the variable
        self.__DoB = DoB 
        self.__gender = gender
        Person.personCount += 1 #cannot be self or else make its own new variable
    
    #methods
    def walk(self):
        print ("The person is walking")
    def run(self):
        print("The person is running")

    #getters and setters
    def getName(self): #getters
        return self.__name
    def getDoB (self):
        return self.__DoB
    def getGender (self):
        return self.__gender
    
    def setName(self, newName): #set for name
        self.__name = newName

    def printDetails(self):
        print(f"Name: {self.__name} DOB: {self.__DoB} Gender: {self.__gender}")

person1 = Person("Kayleen", "16/05/2008", "Female")
person2 = Person("Mark", "05/12/1998", "Male")
person3 = Person("Peter", "19/04/2028", "Male")

print(person1.getName(), person1.getDoB(), person1.getGender())
#method 2:
print(person1.__dict__)
#method 3:
person1.printDetails()
