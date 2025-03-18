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
        AllEmployees[index].ChangeDepartment(NewDepartment)
        #(g)
        print (f"{AllEmployees[index].GetName} ({AllEmployees[index].GetEmployeeID}) has changed department to {AllEmployees[index].GetDepartment}")
    else:
        print ("Invalid mode")

#Q2

#(a)
QueueData = [0 for i in range(8)]
QueueFront = -1
QueueRear = -1

#(b)
def allElements(QueueData, QueueFront, QueueRear):
    for i in range (QueueFront, QueueRear):
        print(QueueData[i])
        i = i +1 
    print (f"Queue Front is at {QueueFront}")
    print (f"Queue Rear is at {QueueRear}")
    print(f"The number of elements are {i}")

#(c)
def Enqueue(NewElement):
    maxsize = len(QueueData)
    global maxsize
    if maxsize == i : #i is length of queue
        return False
    elif QueueRear == maxsize -1 :
        QueueRear = 0
    else:
        QueueRear = QueueRear + 1
    QueueData[QueueRear] = NewElement
    i = i + 1
    return True

#(d)(i)
for u in range (9):
    NewElement = int(input("Input a new element: "))
    result = Enqueue(NewElement)
    if result == False:
        print("Element could not be added")
    else:
        print("Element is added")
    
for u in range(9):
    print(QueueData[u])
print(f"Front Pointer: {QueueFront}")
print(f"Rear Pointer: {QueueRear}")
print(f"The number of elements in the array {i}")

#(d)(ii)

#(e)(i)
def Dequeue():
    if i == 0:
        return -1
    else:
        temp = QueueData[i]
        QueueData[i] = None
        i = i - 1
        if QueueFront == maxsize
        QueueFront = QueueFront + 1
        ########

#(e)(ii)
#####

#Q3

#(a)

