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
def Procedure():
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
    except:
        print("No file found")
