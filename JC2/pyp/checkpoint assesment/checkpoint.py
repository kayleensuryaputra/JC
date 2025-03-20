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

file = open("C:/Users/Kayleen JC2T/Desktop/JC/JC2/pyp/checkpoint assesment/Employees.txt",'r')
for i in range(10):
    AllEmployees[i].ChangeName(file.readline().strip()) #no need to pass self anym
    AllEmployees[i].ChangeEmployeeID(file.readline().strip())
    AllEmployees[i].ChangeDepartment(file.readline().strip())

#(e)

SearchUser = input("Input Employee to be searched: ")
for i in range (10):
    if SearchUser == AllEmployees[i].GetName():
        index = i

#(f)
Mode = ""
while Mode != 'P' and Mode != 'D':
    Mode = input("Input mode to be done: ")
    if Mode == 'P':
        print(f"Name of Employee: {AllEmployees[index].GetName()}")
        print(f"ID of Employee: {AllEmployees[index].GetEmployeeID()}")  
        print(f"Department of Employee: {AllEmployees[index].GetDepartment()}")
    elif Mode == 'D':
        NewDepartment = input("Input a new department: ")
        AllEmployees[index].ChangeDepartment(NewDepartment)
        #(g)
        print (f"{AllEmployees[index].GetName()} ({AllEmployees[index].GetEmployeeID()}) has changed department to {AllEmployees[index].GetDepartment()}")
    else:
        print ("Invalid mode")

#Q2

#(a)
QueueData = [0 for i in range(8)]
QueueFront = -1
QueueRear = -1

#not part of (a)
QueueLength = 0 
maxsize = len(QueueData)

#(b)
def allElements(QueueData, QueueFront, QueueRear):
    # #no need to print one by one
    # for i in range (QueueFront, QueueRear):
    #     print(QueueData[i])
    #     i = i +1 
    
    #just print everything at once
    print(QueueData)

    print (f"Queue Front is at {QueueFront}")
    print (f"Queue Rear is at {QueueRear}")
    print(f"The number of elements are {QueueLength}")

#(c)
def Enqueue(NewElement):
    if QueueLength == maxsize: #i is length of queue
        return False
    elif QueueRear == maxsize -1 :
        QueueRear = 0
    else:
        QueueRear = QueueRear + 1
    QueueData[QueueRear] = NewElement
    QueueLength = QueueLength + 1
    return True

#(d)(i)
for i in range (9):
    NewElement = int(input("Input a new element: "))
    result = Enqueue(NewElement)
    if result == False:
        print("Element could not be added")
    else:
        print("Element is added")
    
allElements()

#(d)(ii)
#screenshot result

#(e)(i)
def Dequeue():
    temp = QueueData[QueueFront] #store the initiaal value temporarily
    if QueueLength == 0:
        return -1
    else:
        temp = QueueData[QueueFront]
        QueueData[QueueFront] = None #not necessary to include, can just ignore
        if QueueFront == maxsize:
            QueueFront = 0 #circular queue
        else:
            QueueFront += 1
            QueueLength -= 1
        return temp

#(e)(ii)
#screenshot result

#Q3

#(a)
myArray = [0 for i in range(10)]

#(b)
def ReadNumbers():
    file = open("Numbers.txt",'r')
    for i in range (10):
         text = file.readline()
         myArray[i] = int(text.strip())

#(c)
def OutputNumbers():
    print(myArray)

#(d)(i)
ReadNumbers()
OutputNumbers()

#(d)(ii)
#screenshot the result 

#(e)
def InsertionSort():
    for i in range (1,len(myArray)):
        key = myArray[i]
        j = i - 1
        while (key < myArray[j]) and (j >= 0):
            temp = myArray[j]
            myArray[j] = myArray[j+1]
            myArray[j+1] = temp
            j = j-1
    print(myArray)

#(f)
