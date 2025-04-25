#(a)
BeverageQueue = ["" for i in range(10)] #of type integer
BeverageFrontPointer = 0
BeverageRearPointer = 0

#(b)(i)
def DisplayMenu():
    try:
        menu = open("BeverageData.txt", 'r')
        print(menu.read())
        menu.close()
    except:
        print("No file found")

DisplayMenu()

#(b)(ii)
def TakeOrder():
    try:
        menu = open("Beverage.txt",'r')
        order = open("Order.txt", 'a')
        customer = input("Input beverages wanted: ")
        beverage = customer.split(',') #considered as an array
        line = menu.readline().strip()
        while line != "":
            for i in range (len(beverage)):
                if beverage[i] == line:
                    order.write(f"{beverage[i]}\n")
            line = menu.readline().strip()
        menu.close()
        order.close()
    except:
        print("No file found")

#(b)(iii)
def EnqueueBeverage(DataToEnqueue):
    if BeverageRearPointer == 10:
        return False
    else:
        BeverageQueue[BeverageRearPointer] = DataToEnqueue
        BeverageRearPointer = BeverageRearPointer + 1
        return True

#(b)(iv)
def ReadOrderData():
    try:
        order = open("Order.txt",'r')
        line = order.readline().strip()
        EnqueueBeverage(line)
        order.close()
    except:
        print ("File not found")

#(c)(i)
def DequeueBeverage():
    ReturnData = "" #of type of string
    if BeverageFrontPointer == BeverageRearPointer:
        return ""
    else:
        ReturnData = BeverageQueue[BeverageFrontPointer]
        BeverageFrontPointer = BeverageFrontPointer + 1
        return ReturnData

#(c)(ii)
def ServeItem():
    item = DequeueBeverage()
    if item == "":
        print("No more order to serve")
    else:
        print(f"You ordered {item}")

#(d)(i)
DisplayMenu()
TakeOrder()
ReadOrderData()
ServeItem()

