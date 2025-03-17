#Q1

#(a)
class Employee:
    def __init__(self, Name, EmployeeID, Department):
        self.__Name = Name #of type string
        self.__EmployeeID = EmployeeID #of type integer
        self.__Department = Department #of type string

#(b)  
    def GetName(self):
        return self.__Name
    
    def GetEmployeeID(self):
        return self.__EmployeeID
    
    def GetDepartment(self):
        return self.__Department

#(c) 
    def ChangeDepartment(self, NewDepartment):
        self.__Department = NewDepartment

#fslkdjflksjdlkfslf
    def ChangeName(self,NewName):
        self.__Name = NewName
    
    def ChangeEmployeeID(self,NewID):
        self.__EmployeeID = NewID

#(d)
AllEmployees = [Employee("", 0, "") for i in range (10)]

file = open("EmployeeFile.txt",'r')
for i in range(10):
    AllEmployees[i].ChangeName(file.readline().strip()) #no need to pass self anym
    AllEmployees[i].ChangeEmployeeID(file.readline().strip())
    AllEmployees[i].ChangeDepartment(file.readline().strip())

#(e)

SearchUser = input("Input Employee to be searched: ")
for i in range (10):
    if SearchUser == AllEmployees[i].GetName():
        index = i
    else:
        i = i +1

#(f)
Mode = ""
while Mode != 'P' and Mode != 'D':
    Mode = input("Input mode to be done: ")
    if Mode == 'P':
        print(f"Name of Employee: {AllEmployees[index].GetName}")
        print(f"ID of Employee: {AllEmployees[index].GetEmployeeID}")  
        print(f"Department of Employee: {AllEmployees[index].GetDepartment}")
    elif Mode == 'D':
        NewDepartment = input("Input a new department: ")
        AllEmployees[i].ChangeDepartment(NewDepartment)
    else:
        print ("Invalid mode")

