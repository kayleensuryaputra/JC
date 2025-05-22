#(a)
class SaleData():
    def __init__(self, saleID, quantity):
        self.saleID = saleID
        self.quantity = quantity

#(b)
CircularQueue = [SaleData("",0) for i in range (5)]
Head = 0 #of type integer
Tail = 0 #of type integer
NumberOfItems = 0 #of type integer
for i in range (5):
    CircularQueue[i].saleID = ""
    CircularQueue[i].quantity = 0

#(c)
def Enqueue(ID, quantity):
    global Tail
    if Tail == len(CircularQueue):
        Tail = 0
    else:
        Tail = Tail - 1
    
    if Tail == Head:
        return -1
    else:
        CircularQueue[Tail].saleID = ID
        CircularQueue[Tail].quantity = quantity
        return 1

#(d)
def Dequeue():
    if Head == -1:
        return -1
    else:
        temporary = Head
        Head = Head + 1
        return CircularQueue[temporary]

#(e)
def EnterRecord(ID, quantity):
    result = Enqueue(ID, quantity)
    if result == -1:
        print("Full")
    else:
        print("Stored")

#(f)(i)
EnterRecord("ADF",10)
EnterRecord("OOP",1)
EnterRecord("BXW",5)
EnterRecord("XXZ",22)
EnterRecord("HQR",6)
EnterRecord("LLP",3)
value = Dequeue()
if value == -1:
    print("Circular Queue is empty")
else:
    print(value.saleID, value.quantity)
EnterRecord("LLP",3)
for i in range (len(CircularQueue)):
    print(CircularQueue[i].saleID, CircularQueue[i].quantity)


#(f)(ii) - SS output