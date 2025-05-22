#(a)
QueueData = ["" for i in range(20)]
QueueHead = -1 
QueueTail = -1
length = 0

#(b)
def Enqueue(data):
    if length == len(QueueData):
        return False
    else:
        Enqueue[QueueTail] = data
        length = length + 1
        if QueueTail == len(QueueData) and not QueueHead == QueueTail:
            QueueTail = 0
        else:
            QueueTail = QueueTail + 1
        if QueueHead == -1:
            QueueHead = 0
        return True

#(c)
def Dequeue():
    if length == 0:
        return "false"
    else:
        temp = QueueHead
        if QueueHead == len(QueueData) and not QueueTail==0:
            QueueHead = 0
        else:
            QueueHead = QueueHead + 1
        return QueueData[temp]

#(d)(i)
def StoreItems(string):
    even = 0
    odd = 0
    totalE = 0
    totalO = 0
    for i in range (7):
        value = string[i]
        if i == 0 or 2 or 4:
            even = int(value)*1 
            totalE = totalE + even
        elif i == 1 or 3 or 5:
            odd = int(value)*3
            totalO = totalO + odd
        else:
            check = value
    if check == 10:
        check = 'X'
    elif check == (totalE+totalO//10):
        for i in range[6]:
            newstr = newstr + string[i]
            Enqueue(newstr)
    else:
        invalid = invalid + 1
    print(f"Number of invalid: {invalid}")

#(d)(ii)
StoreItems("999999X")
result = Dequeue()
if result == "false":
    print("Queue is empty")
else:
    print(result)

            

#hardcode
print("999999X")
print(f"Number of invalid: {}")

# print("Queue is empty")
print("[string]")
