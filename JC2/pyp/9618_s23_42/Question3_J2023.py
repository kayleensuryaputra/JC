#(a)(i)
class Employee():
    def __init__(self,HourlyPay, EmployeeNumber, JobTitle,PayYear2022):
        self.__HourlyPay = HourlyPay #of type real
        self.__EmployeeNumber = EmployeeNumber #of type string
        self.__JobTitle = JobTitle #of type string
        self.__PayYear2022 = [0.0 for i in range(52)] #of type real
#(a)(ii)
    def GetEmployeeNumber(self):
        return self.__EmployeeNumber
#(a)(iii)    
    def SetPay(self, WeekNum,HoursWorked):
        Pay = HoursWorked* self.__HourlyPay
        self.__PayYear2022[WeekNum] = Pay
#(a)(iv)    
    def GetTotalPay(self,WeekNum):
        total = 0
        for i in range (WeekNum):
            value = self.__PayYear2022[WeekNum]
            total = total + value
        return total
    
#(b)(i)
class Manager(Employee):
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle,BonusValue):
        super().__init__(HourlyPay, EmployeeNumber, JobTitle) #remove 2022 array
        self.__BonusValue = BonusValue #of type real
#(b)(ii)
#     def SetPay(self,WeekNum, HoursWorked): [have to refer to the super class]
        # Pay = HoursWorked* self.HourlyPay
        # self.PayYear2022[WeekNum] = Pay*(self.BonusValue/100) + Pay
    
    def SetPay(self, WeekNum, HoursWorked):
        return super().SetPay(WeekNum, HoursWorked*(1 + self.__BonusValue/100))

#(c)
EmployeeArray = [Employee() for i in range(8)]
try:
    file = open ("Employees.txt", 'r')
    for i in range (8):
        hourlypay = file.readline().strip()
        employeenum = file.readline().strip()
        value = file.readline().strip()
        try:
            test = float(value)
            bonus = test
            title = file.readline().strip()
            EmployeeArray[i] = Manager(hourlypay,employeenum,bonus,title)
        except:
            EmployeeArray[i] = Employee(hourlypay,employeenum,value)
    file.close()
except:
    print ("file not found")

#(d)
def EnterHours():
    try:
        file = open("HoursWeek1.txt",'r')
        for i in range (8):
            id = file.readline().strip()
            if EmployeeArray[i].GetEmployeeNumber() == id:
                hours = file.readline().strip()
                EmployeeArray[i].SetPay(1,hours)
            else:
                i = i + 1
    except:
        print("File not found")

#(e)
EnterHours()
for i in range (8):
    id = EmployeeArray[i].__EmployeeNumber
    value = EmployeeArray[i].GetTotalPay()
    print(f"Employee ID: {id} Total Pay: {value}")