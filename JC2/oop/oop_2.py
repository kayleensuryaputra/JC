class Person:
    personCount = 0 # class variable
    def __init__(self, name, DoB, gender):
        #instance variables / object variables
        self.__name = name #__ to private the variable
        self.__DoB = DoB 
        self.__gender = gender
        Person.personCount += 1 #cannot be self or else make its own new variable
    def walk():
        print ("The person is walking")
    def run():
        print("The person is running")
    #getters and setters
    def getName(self): #getters
        return self.__name
    def getDoB (self):
        return self.__DoB
    def getGender (self):
        return self.__gender
    
    def setName(self, newName):

person1 = Person("Kayleen", "16/05/2008", "Female")

print(person1.getName(), person1.getDoB(), person1.getGender())
#another method:
# print(person1)

person1.setName("Alex")