#(a)
class Queue:
    def __init__(self,QueueArray,Headpointer,Tailpointer):
        self.__QueueArray = [0 for i in range(100)] #of type integer
        self.__Headpointer = Headpointer #of type integer
        self.__Tailpointer = Tailpointer #of type integer
    # def GetHead(self):
    #     return self.__Headpointer
    

#(b)
TheQueue = Queue([-1 for i in range(100)],-1,0)

#(c)
def Enqueue(AQueue,TheData):
    if AQueue.Headpointer == -1:
        AQueue.QueueArray[AQueue.Tailpointer] = TheData
        AQueue.Headpointer = 0
        AQueue.Tailpointer = AQueue.Tailpointer + 1
        return 1
    elif AQueue.Tailpointer > len(AQueue.QueueArray):
        return -1
    else:
        AQueue.QueueArray[AQueue.Tailpointer] = TheData
        AQueue.Tailpointer = AQueue.Tailpointer + 1
        return 1

#(d)
def ReturnAllData():
    if TheQueue.Headpointer == 100:
        return ""
    for i in range(TheQueue.Headpointer,100):
        value = str(TheQueue.QueueArray[i]) #do i need to make a QueueArray getter?
        return ReturnAllData(value+"")

#(e)(i)
value = int(input("Input a value: "))
for i in range(10):
    while value < 0:
        value = int(input("Input a value: "))
    result = Enqueue(TheQueue,value)
    if result == -1:
        print("Queue is full")
    else:
        print("Value stored")
print(ReturnAllData())

#(e)(ii) - SS OUTPUT [cannot]

#(f)
def Dequeue(TheQueue):
    if TheQueue.Headpointer == -1 and TheQueue.Tailpointer ==0:
        return -1
    else:
        temp = TheQueue.Headpointer
        TheQueue.Headpointer = TheQueue.Headpointer + 1
        result = TheQueue.QueueArray[temp]
        return result

#(g)(i)
for i in range (2):
    result = Dequeue()
    if result == -1:
        print("Queue is empty")
    else:
        print(result)
ReturnAllData()

#(g)(ii) - SS OUTPUT [cannot]


# #hardcode
# print("Queue is full")
# print("Value stored")