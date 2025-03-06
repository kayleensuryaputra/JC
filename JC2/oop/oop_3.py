#CREATE A SUB CLASS 'Teacher' USING SUPER CLASS 'Person'

class Person:
    def __init__(self, name, DoB, gender):
        self.__name = name 
        self.__DoB = DoB 
        self.__gender = gender
    
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

    def printDetails(self):
        print(f"Name: {self.__name} DOB: {self.__DoB} Gender: {self.__gender}")

#All the constructor and variables same as Person
# class Teacher(Person):
#     pass #constructor used from Person class

# teacher1 = Teacher("Allan", "12/06/1990", "Male")
# teacher1.printDetails()

#To change the Instance Variable
class Teacher(Person):
    def __init__(self, name, DoB, gender, salary):
        super().__init__(name, DoB, gender) #copies the properties from Person
        self.salary = salary #added salary into the variable; dont forget to pass as well

    #polymorphism of printDetails from Person()
    def printDetails(self):
        print(f"Name: {self.getName()} DOB: {self.getDoB()} Gender: {self.getGender()} Salary: {self.salary}") 

teacher1 = Teacher("Allan", "12/06/1990", "Male", 2000)
teacher1.printDetails()

class Student(Person):
    def __init__(self, name, DoB, gender, grade): #pass 'grade' as well
        super().__init__(name, DoB, gender)
        self.grade = grade
    
    def printDetails(self):
        print(f"Name: {self.getName()} DOB: {self.getDoB()} Gender: {self.getGender()} Grades: {self.grade}") 

student1 = Student("Kayleen", "16/05/2008", "Female", 100)
student1.printDetails()